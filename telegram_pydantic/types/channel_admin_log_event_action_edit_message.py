from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionEditMessage(BaseModel):
    """
    types.ChannelAdminLogEventActionEditMessage
    ID: 0x709b2405
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionEditMessage', 'ChannelAdminLogEventActionEditMessage'] = pydantic.Field(
        'types.ChannelAdminLogEventActionEditMessage',
        alias='_'
    )

    prev_message: "base.Message"
    new_message: "base.Message"
