from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# JSONValue - Layer 181
JSONValue = typing.Annotated[
    typing.Union[
        typing.Annotated[types.JsonArray, pydantic.Tag('JsonArray')],
        typing.Annotated[types.JsonBool, pydantic.Tag('JsonBool')],
        typing.Annotated[types.JsonNull, pydantic.Tag('JsonNull')],
        typing.Annotated[types.JsonNumber, pydantic.Tag('JsonNumber')],
        typing.Annotated[types.JsonObject, pydantic.Tag('JsonObject')],
        typing.Annotated[types.JsonString, pydantic.Tag('JsonString')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
