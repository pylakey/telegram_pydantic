from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class VideoSizeEmojiMarkup(BaseModel):
    """
    types.VideoSizeEmojiMarkup
    ID: 0xf85c413c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.VideoSizeEmojiMarkup', 'VideoSizeEmojiMarkup'] = pydantic.Field(
        'types.VideoSizeEmojiMarkup',
        alias='_'
    )

    emoji_id: int
    background_colors: list[int]
