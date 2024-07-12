from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEvent(BaseModel):
    """
    types.ChannelAdminLogEvent
    ID: 0x1fad68cd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEvent', 'ChannelAdminLogEvent'] = pydantic.Field(
        'types.ChannelAdminLogEvent',
        alias='_'
    )

    id: int
    date: Datetime
    user_id: int
    action: "base.ChannelAdminLogEventAction"
