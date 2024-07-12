from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BroadcastRevenueWithdrawalUrl(BaseModel):
    """
    types.stats.BroadcastRevenueWithdrawalUrl
    ID: 0xec659737
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stats.BroadcastRevenueWithdrawalUrl', 'BroadcastRevenueWithdrawalUrl'] = pydantic.Field(
        'types.stats.BroadcastRevenueWithdrawalUrl',
        alias='_'
    )

    url: str
