from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionStopPoll(BaseModel):
    """
    types.ChannelAdminLogEventActionStopPoll
    ID: 0x8f079643
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionStopPoll', 'ChannelAdminLogEventActionStopPoll'] = pydantic.Field(
        'types.ChannelAdminLogEventActionStopPoll',
        alias='_'
    )

    message: "base.Message"
