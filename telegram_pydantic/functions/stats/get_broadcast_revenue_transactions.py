from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBroadcastRevenueTransactions(BaseModel):
    """
    functions.stats.GetBroadcastRevenueTransactions
    ID: 0x69280f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetBroadcastRevenueTransactions', 'GetBroadcastRevenueTransactions'] = pydantic.Field(
        'functions.stats.GetBroadcastRevenueTransactions',
        alias='_'
    )

    channel: "base.InputChannel"
    offset: int
    limit: int
