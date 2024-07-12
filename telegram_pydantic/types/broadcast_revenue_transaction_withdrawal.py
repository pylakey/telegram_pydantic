from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BroadcastRevenueTransactionWithdrawal(BaseModel):
    """
    types.BroadcastRevenueTransactionWithdrawal
    ID: 0x5a590978
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BroadcastRevenueTransactionWithdrawal', 'BroadcastRevenueTransactionWithdrawal'] = pydantic.Field(
        'types.BroadcastRevenueTransactionWithdrawal',
        alias='_'
    )

    amount: int
    date: Datetime
    provider: str
    pending: typing.Optional[bool] = None
    failed: typing.Optional[bool] = None
    transaction_date: Datetime
    transaction_url: typing.Optional[str] = None
