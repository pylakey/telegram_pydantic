from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class VideoSizeStickerMarkup(BaseModel):
    """
    types.VideoSizeStickerMarkup
    ID: 0xda082fe
    Layer: 181
    """
    QUALNAME: typing.Literal['types.VideoSizeStickerMarkup', 'VideoSizeStickerMarkup'] = pydantic.Field(
        'types.VideoSizeStickerMarkup',
        alias='_'
    )

    stickerset: "base.InputStickerSet"
    sticker_id: int
    background_colors: list[int]
