from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BroadcastRevenueTransactions(BaseModel):
    """
    types.stats.BroadcastRevenueTransactions
    ID: 0x87158466
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stats.BroadcastRevenueTransactions', 'BroadcastRevenueTransactions'] = pydantic.Field(
        'types.stats.BroadcastRevenueTransactions',
        alias='_'
    )

    count: int
    transactions: list["base.BroadcastRevenueTransaction"]
