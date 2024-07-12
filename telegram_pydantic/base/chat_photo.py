from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ChatPhoto - Layer 181
ChatPhoto = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ChatPhoto, pydantic.Tag('ChatPhoto')],
        typing.Annotated[types.ChatPhotoEmpty, pydantic.Tag('ChatPhotoEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
