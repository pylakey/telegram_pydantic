from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeEmojiStatus(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeEmojiStatus
    ID: 0x3ea9feb1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeEmojiStatus', 'ChannelAdminLogEventActionChangeEmojiStatus'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeEmojiStatus',
        alias='_'
    )

    prev_value: "base.EmojiStatus"
    new_value: "base.EmojiStatus"
