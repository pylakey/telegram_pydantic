from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# photos.Photos - Layer 181
Photos = typing.Annotated[
    typing.Union[
        typing.Annotated[types.photos.Photos, pydantic.Tag('photos.Photos')],
        typing.Annotated[types.photos.PhotosSlice, pydantic.Tag('photos.PhotosSlice')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
