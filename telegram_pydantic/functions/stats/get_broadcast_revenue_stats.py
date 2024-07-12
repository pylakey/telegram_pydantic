from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBroadcastRevenueStats(BaseModel):
    """
    functions.stats.GetBroadcastRevenueStats
    ID: 0x75dfb671
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetBroadcastRevenueStats', 'GetBroadcastRevenueStats'] = pydantic.Field(
        'functions.stats.GetBroadcastRevenueStats',
        alias='_'
    )

    channel: "base.InputChannel"
    dark: typing.Optional[bool] = None
