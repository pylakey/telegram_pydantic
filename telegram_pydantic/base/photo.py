from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# Photo - Layer 181
Photo = typing.Annotated[
    typing.Union[
        typing.Annotated[types.Photo, pydantic.Tag('Photo')],
        typing.Annotated[types.PhotoEmpty, pydantic.Tag('PhotoEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
