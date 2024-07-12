from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BroadcastRevenueTransactionRefund(BaseModel):
    """
    types.BroadcastRevenueTransactionRefund
    ID: 0x42d30d2e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BroadcastRevenueTransactionRefund', 'BroadcastRevenueTransactionRefund'] = pydantic.Field(
        'types.BroadcastRevenueTransactionRefund',
        alias='_'
    )

    amount: int
    date: Datetime
    provider: str
