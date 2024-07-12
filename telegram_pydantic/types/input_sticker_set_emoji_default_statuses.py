from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetEmojiDefaultStatuses(BaseModel):
    """
    types.InputStickerSetEmojiDefaultStatuses
    ID: 0x29d0f5ee
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetEmojiDefaultStatuses', 'InputStickerSetEmojiDefaultStatuses'] = pydantic.Field(
        'types.InputStickerSetEmojiDefaultStatuses',
        alias='_'
    )

