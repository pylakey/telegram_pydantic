from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# VideoSize - Layer 181
VideoSize = typing.Annotated[
    typing.Union[
        typing.Annotated[types.VideoSize, pydantic.Tag('VideoSize')],
        typing.Annotated[types.VideoSizeEmojiMarkup, pydantic.Tag('VideoSizeEmojiMarkup')],
        typing.Annotated[types.VideoSizeStickerMarkup, pydantic.Tag('VideoSizeStickerMarkup')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
