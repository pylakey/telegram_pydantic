from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BroadcastRevenueTransactionProceeds(BaseModel):
    """
    types.BroadcastRevenueTransactionProceeds
    ID: 0x557e2cc4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BroadcastRevenueTransactionProceeds', 'BroadcastRevenueTransactionProceeds'] = pydantic.Field(
        'types.BroadcastRevenueTransactionProceeds',
        alias='_'
    )

    amount: int
    from_date: Datetime
    to_date: Datetime
