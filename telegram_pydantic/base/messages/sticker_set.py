from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.StickerSet - Layer 181
StickerSet = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.StickerSet, pydantic.Tag('messages.StickerSet')],
        typing.Annotated[types.messages.StickerSetNotModified, pydantic.Tag('messages.StickerSetNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
