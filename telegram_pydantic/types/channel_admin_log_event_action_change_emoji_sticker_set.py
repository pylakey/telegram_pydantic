from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeEmojiStickerSet(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeEmojiStickerSet
    ID: 0x46d840ab
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeEmojiStickerSet', 'ChannelAdminLogEventActionChangeEmojiStickerSet'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeEmojiStickerSet',
        alias='_'
    )

    prev_stickerset: "base.InputStickerSet"
    new_stickerset: "base.InputStickerSet"
