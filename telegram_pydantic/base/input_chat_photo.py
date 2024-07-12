from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputChatPhoto - Layer 181
InputChatPhoto = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputChatPhoto, pydantic.Tag('InputChatPhoto')],
        typing.Annotated[types.InputChatPhotoEmpty, pydantic.Tag('InputChatPhotoEmpty')],
        typing.Annotated[types.InputChatUploadedPhoto, pydantic.Tag('InputChatUploadedPhoto')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
