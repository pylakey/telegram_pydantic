from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CollectibleInfo(BaseModel):
    """
    types.fragment.CollectibleInfo
    ID: 0x6ebdff91
    Layer: 181
    """
    QUALNAME: typing.Literal['types.fragment.CollectibleInfo', 'CollectibleInfo'] = pydantic.Field(
        'types.fragment.CollectibleInfo',
        alias='_'
    )

    purchase_date: Datetime
    currency: str
    amount: int
    crypto_currency: str
    crypto_amount: int
    url: str
