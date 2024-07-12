from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BroadcastRevenueStats(BaseModel):
    """
    types.stats.BroadcastRevenueStats
    ID: 0x5407e297
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stats.BroadcastRevenueStats', 'BroadcastRevenueStats'] = pydantic.Field(
        'types.stats.BroadcastRevenueStats',
        alias='_'
    )

    top_hours_graph: "base.StatsGraph"
    revenue_graph: "base.StatsGraph"
    balances: "base.BroadcastRevenueBalances"
    usd_rate: float
