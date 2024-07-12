from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBroadcastRevenueTransactions(BaseModel):
    """
    types.UpdateBroadcastRevenueTransactions
    ID: 0xdfd961f5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBroadcastRevenueTransactions', 'UpdateBroadcastRevenueTransactions'] = pydantic.Field(
        'types.UpdateBroadcastRevenueTransactions',
        alias='_'
    )

    peer: "base.Peer"
    balances: "base.BroadcastRevenueBalances"
