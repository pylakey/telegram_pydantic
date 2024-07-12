from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeHistoryTTL(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeHistoryTTL
    ID: 0x6e941a38
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeHistoryTTL', 'ChannelAdminLogEventActionChangeHistoryTTL'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeHistoryTTL',
        alias='_'
    )

    prev_value: int
    new_value: int
