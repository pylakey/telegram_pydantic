from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetEmojiChannelDefaultStatuses(BaseModel):
    """
    types.InputStickerSetEmojiChannelDefaultStatuses
    ID: 0x49748553
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetEmojiChannelDefaultStatuses', 'InputStickerSetEmojiChannelDefaultStatuses'] = pydantic.Field(
        'types.InputStickerSetEmojiChannelDefaultStatuses',
        alias='_'
    )

