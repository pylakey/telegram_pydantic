from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# PhotoSize - Layer 181
PhotoSize = typing.Annotated[
    typing.Union[
        typing.Annotated[types.PhotoCachedSize, pydantic.Tag('PhotoCachedSize')],
        typing.Annotated[types.PhotoPathSize, pydantic.Tag('PhotoPathSize')],
        typing.Annotated[types.PhotoSize, pydantic.Tag('PhotoSize')],
        typing.Annotated[types.PhotoSizeEmpty, pydantic.Tag('PhotoSizeEmpty')],
        typing.Annotated[types.PhotoSizeProgressive, pydantic.Tag('PhotoSizeProgressive')],
        typing.Annotated[types.PhotoStrippedSize, pydantic.Tag('PhotoStrippedSize')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
