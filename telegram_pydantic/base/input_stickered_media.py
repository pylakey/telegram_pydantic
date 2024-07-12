from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputStickeredMedia - Layer 181
InputStickeredMedia = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputStickeredMediaDocument, pydantic.Tag('InputStickeredMediaDocument')],
        typing.Annotated[types.InputStickeredMediaPhoto, pydantic.Tag('InputStickeredMediaPhoto')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
