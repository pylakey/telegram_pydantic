from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBroadcastRevenueWithdrawalUrl(BaseModel):
    """
    functions.stats.GetBroadcastRevenueWithdrawalUrl
    ID: 0x2a65ef73
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetBroadcastRevenueWithdrawalUrl', 'GetBroadcastRevenueWithdrawalUrl'] = pydantic.Field(
        'functions.stats.GetBroadcastRevenueWithdrawalUrl',
        alias='_'
    )

    channel: "base.InputChannel"
    password: "base.InputCheckPasswordSRP"
