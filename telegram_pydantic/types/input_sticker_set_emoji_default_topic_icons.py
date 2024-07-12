from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetEmojiDefaultTopicIcons(BaseModel):
    """
    types.InputStickerSetEmojiDefaultTopicIcons
    ID: 0x44c1f8e9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetEmojiDefaultTopicIcons', 'InputStickerSetEmojiDefaultTopicIcons'] = pydantic.Field(
        'types.InputStickerSetEmojiDefaultTopicIcons',
        alias='_'
    )

