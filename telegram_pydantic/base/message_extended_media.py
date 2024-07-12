from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# MessageExtendedMedia - Layer 181
MessageExtendedMedia = typing.Annotated[
    typing.Union[
        typing.Annotated[types.MessageExtendedMedia, pydantic.Tag('MessageExtendedMedia')],
        typing.Annotated[types.MessageExtendedMediaPreview, pydantic.Tag('MessageExtendedMediaPreview')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
