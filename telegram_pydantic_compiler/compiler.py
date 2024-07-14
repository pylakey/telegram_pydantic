#  Pylogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2023 Dan <https://github.com/delivrance>
#  Copyright (C) 2023-2024 Pylakey <https://github.com/pylakey>
#
#  This file is part of Pylogram.
#
#  Pylogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pylogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pylogram.  If not, see <http://www.gnu.org/licenses/>.

import json
import os
import re
import shutil
from functools import partial
from pathlib import Path
from typing import List
from typing import NamedTuple
from typing import Tuple

# from autoflake import fix_code
# from black import format_str, FileMode

HOME_PATH = Path(__file__).parent
DESTINATION_PATH = Path("telegram_pydantic")

SECTION_RE = re.compile(r"---(\w+)---")
LAYER_RE = re.compile(r"//\sLAYER\s(\d+)")
COMBINATOR_RE = re.compile(r"^([\w.]+)#([0-9a-f]+)\s(?:.*)=\s([\w<>.]+);$", re.MULTILINE)
ARGS_RE = re.compile(r"[^{](\w+):([\w?!.<>#]+)")
FLAGS_RE = re.compile(r"flags(\d?)\.(\d+)\?")
FLAGS_RE_2 = re.compile(r"flags(\d?)\.(\d+)\?([\w<>.]+)")
FLAGS_RE_3 = re.compile(r"flags(\d?):#")
INT_RE = re.compile(r"int(\d+)")

CORE_TYPES = ["int", "long", "int128", "int256", "double", "bytes", "string", "Bool", "true"]

# noinspection PyShadowingBuiltins
open = partial(open, encoding="utf-8")

types_to_constructors = {}
types_to_functions = {}
constructors_to_functions = {}
namespaces_to_types = {}
namespaces_to_constructors = {}
namespaces_to_functions = {}

try:
    with open("docs.json") as f:
        docs = json.load(f)
except FileNotFoundError:
    docs = {
        "type": {},
        "constructor": {},
        "method": {}
    }


class Combinator(NamedTuple):
    section: str
    qualname: str
    namespace: str
    name: str
    id: str
    has_flags: bool
    args: List[Tuple[str, str]]
    qualtype: str
    typespace: str
    type: str


def snake(s: str):
    # https://stackoverflow.com/q/1175208
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s).lower()


def camel(s: str):
    return "".join([i[0].upper() + i[1:] for i in s.split("_")])


# noinspection PyShadowingBuiltins, PyShadowingNames
def get_type_hint(type: str) -> tuple[str, bool]:
    is_flag = bool(FLAGS_RE.match(type))
    is_core = False

    if is_flag:
        type = type.split("?")[1]

    if type in CORE_TYPES:
        is_core = True

        if type == "long" or "int" in type:
            type = "int"
        elif type == "double":
            type = "float"
        elif type == "string":
            type = "str"
        elif type in ["Bool", "true"]:
            type = "bool"
        else:  # bytes and object
            type = "Bytes"

    if type == "date":
        # OR Custom datetime type
        return "Datetime", is_flag

    if type in ["Object", "!X"]:
        return "BaseModel", is_flag

    if re.match("^vector", type, re.I):
        is_core = True

        sub_type = type.split("<")[1][:-1]
        subtype_hint, is_optional = get_type_hint(sub_type)

        if is_optional:
            subtype_hint = f"typing.Optional[{subtype_hint}]"

        type = f"list[{subtype_hint}]"

    if is_core:
        return type, is_flag
    else:
        ns, name = type.split(".") if "." in type else ("", type)
        type = f'"base.' + ".".join([ns, name]).strip(".") + '"'

        return type, is_flag


def sort_args(args):
    """Put flags at the end"""
    args = args.copy()
    flags = [i for i in args if FLAGS_RE.match(i[1])]

    for i in flags:
        args.remove(i)

    for i in args[:]:
        if re.match(r"flags\d?", i[0]) and i[1] == "#":
            args.remove(i)

    return args + flags


def get_references(t: str, kind: str):
    if kind == "constructors":
        t = constructors_to_functions.get(t)
    elif kind == "types":
        t = types_to_functions.get(t)
    else:
        raise ValueError("Invalid kind")

    if t:
        return "\n            ".join(t), len(t)

    return None, 0


arg_aliases = {
    "from": ["from_peer", 'from_'],
    "self": ["is_self"],
    "json": ["json_"],
}


# noinspection PyShadowingBuiltins
def start(format: bool = False):
    shutil.rmtree(DESTINATION_PATH / "types", ignore_errors=True)
    shutil.rmtree(DESTINATION_PATH / "functions", ignore_errors=True)
    shutil.rmtree(DESTINATION_PATH / "base", ignore_errors=True)

    with open(HOME_PATH / "source/main_api.tl") as f3:
        schema = (f3.read()).splitlines()

    with (
        open(HOME_PATH / "template/base_type.txt") as base_type_template,
        open(HOME_PATH / "template/combinator.txt") as combinator_template,
        open(HOME_PATH / "template/base_union_type.txt") as base_union_type_template,
    ):
        base_type_tmpl = base_type_template.read()
        combinator_tmpl = combinator_template.read()
        base_union_type_tmpl = base_union_type_template.read()

    section = None
    layer = None
    combinators = []

    for line in schema:
        # Check for section changer lines
        section_match = SECTION_RE.match(line)
        if section_match:
            section = section_match.group(1)
            continue

        # Save the layer version
        layer_match = LAYER_RE.match(line)
        if layer_match:
            layer = layer_match.group(1)
            continue

        combinator_match = COMBINATOR_RE.match(line)
        if combinator_match:
            # noinspection PyShadowingBuiltins
            qualname, id, qualtype = combinator_match.groups()

            namespace, name = qualname.split(".") if "." in qualname else ("", qualname)
            name = camel(name)
            qualname = ".".join([namespace, name]).lstrip(".")

            typespace, type = qualtype.split(".") if "." in qualtype else ("", qualtype)
            type = camel(type)
            qualtype = ".".join([typespace, type]).lstrip(".")

            # Pingu!
            has_flags = not not FLAGS_RE_3.findall(line)

            args = ARGS_RE.findall(line)

            combinator = Combinator(
                section=section,
                qualname=qualname,
                namespace=namespace,
                name=name,
                id=f"0x{id}",
                has_flags=has_flags,
                args=args,
                qualtype=qualtype,
                typespace=typespace,
                type=type
            )

            combinators.append(combinator)

    for c in combinators:
        qualtype = c.qualtype

        if qualtype.startswith("Vector"):
            qualtype = qualtype.split("<")[1][:-1]

        d = types_to_constructors if c.section == "types" else types_to_functions

        if qualtype not in d:
            d[qualtype] = []

        d[qualtype].append(c.qualname)

        if c.section == "types":
            key = c.namespace

            if key not in namespaces_to_types:
                namespaces_to_types[key] = []

            if c.type not in namespaces_to_types[key]:
                namespaces_to_types[key].append(c.type)

    for k, v in types_to_constructors.items():
        for i in v:
            try:
                constructors_to_functions[i] = types_to_functions[k]
            except KeyError:
                pass

    for qualtype in types_to_constructors:
        typespace, type = qualtype.split(".") if "." in qualtype else ("", qualtype)
        dir_path = DESTINATION_PATH / "base" / typespace

        module = type

        if module == "Updates":
            module = "UpdatesT"

        os.makedirs(dir_path, exist_ok=True)
        constructors = sorted(types_to_constructors[qualtype])

        if len(constructors) > 1:
            tmpl = base_union_type_tmpl
        else:
            tmpl = base_type_tmpl

        with open(dir_path / f"{snake(module)}.py", "w") as f:
            types = []

            for c in constructors:
                i = " " * 12
                t = (
                    f"typing.Annotated[\n"
                    f"{i}types.{c},\n"
                    f"{i}pydantic.Tag('{c}')"
                )
                only_name = c.split(".")[-1]

                if only_name != c:
                    t += f",\n{i}pydantic.Tag('{only_name}')\n"

                t += f"{' ' * 8}]"
                types.append(t)

            f.write(
                tmpl.format(
                    name=type,
                    qualname=qualtype,
                    types=",\n        ".join(types),
                    layer=layer
                )
            )

    for c in combinators:
        sorted_args = sort_args(c.args)
        arguments = ""

        if sorted_args:
            for i in sorted_args:
                arg_name = i[0]
                arg_type = i[1]

                if "int" in arg_type and (
                        re.search(r'(\b|_)(date|until|since)(\b|_)', arg_name)
                        or arg_name in ('expires', 'expires_at', 'was_online')
                ):
                    arg_type = arg_type.replace('int', 'date')

                type_hint, is_optional = get_type_hint(arg_type)

                if arg_name in arg_aliases:
                    aliases = arg_aliases[arg_name]
                    aliases_string = ", ".join([f"'{a}'" for a in aliases])
                    i = " " * 8
                    default = (
                        f" = pydantic.Field(\n"
                        f"{i}{'None' if is_optional else '...'},\n"
                        f"{i}serialization_alias='{arg_name}',\n"
                        f"{i}validation_alias=pydantic.AliasChoices('{arg_name}', {aliases_string})\n"
                        f"{' ' * 4})"
                    )
                    arg_name = aliases[0]

                else:
                    default = " = None" if is_optional else ""

                if is_optional:
                    type_hint = f"typing.Optional[{type_hint}]"

                arguments += f"\n    {arg_name}: {type_hint}{default}"

        compiled_combinator = combinator_tmpl.format(
            name=c.name,
            id=c.id,
            qualname=f"{c.section}.{c.qualname}",
            arguments=arguments,
            layer=layer
        )

        directory = "types" if c.section == "types" else c.section

        dir_path = DESTINATION_PATH / directory / c.namespace

        os.makedirs(dir_path, exist_ok=True)

        module = c.name

        if module == "Updates":
            module = "UpdatesT"

        with open(dir_path / f"{snake(module)}.py", "w") as f:
            f.write(compiled_combinator)

        d = namespaces_to_constructors if c.section == "types" else namespaces_to_functions

        if c.namespace not in d:
            d[c.namespace] = []

        d[c.namespace].append(c.name)

    for namespace, types in namespaces_to_types.items():
        with open(DESTINATION_PATH / "base" / namespace / "__init__.py", "w") as f:
            for t in types:
                module = t

                if module == "Updates":
                    module = "UpdatesT"

                f.write(f"from .{snake(module)} import {t}\n")

            if not namespace:
                f.write(f"from . import {', '.join(filter(bool, namespaces_to_types))}")

    constructors_rebuilds = []

    for namespace, types in namespaces_to_constructors.items():
        with open(DESTINATION_PATH / "types" / namespace / "__init__.py", "w") as f:
            for t in types:
                module = t

                if module == "Updates":
                    module = "UpdatesT"

                f.write(f"from .{snake(module)} import {t}\n")
                _qualname = f"{namespace}.{t}".lstrip(".")
                constructors_rebuilds.append(f"types.{_qualname}.model_rebuild()")

            if not namespace:
                f.write(f"from . import {', '.join(filter(bool, namespaces_to_constructors))}\n")

    with open(DESTINATION_PATH / "__init__.py", "w") as f:
        f.write(
            f"__version__ = '0.{layer}.0'\n\n"
            "from . import base\n"
            "from . import types\n"
            "from . import functions"
            "\n\n" + "\n".join(constructors_rebuilds) + "\n"
        )

    for namespace, types in namespaces_to_functions.items():
        with open(DESTINATION_PATH / "functions" / namespace / "__init__.py", "w") as f:
            for t in types:
                module = t

                if module == "Updates":
                    module = "UpdatesT"

                f.write(f"from .{snake(module)} import {t}\n")

            if not namespace:
                f.write(f"from . import {', '.join(filter(bool, namespaces_to_functions))}")
