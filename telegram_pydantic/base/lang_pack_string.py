from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# LangPackString - Layer 181
LangPackString = typing.Annotated[
    typing.Union[
        typing.Annotated[types.LangPackString, pydantic.Tag('LangPackString')],
        typing.Annotated[types.LangPackStringDeleted, pydantic.Tag('LangPackStringDeleted')],
        typing.Annotated[types.LangPackStringPluralized, pydantic.Tag('LangPackStringPluralized')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
