from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PremiumSubscriptionOption(BaseModel):
    """
    types.PremiumSubscriptionOption
    ID: 0x5f2d1df2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PremiumSubscriptionOption', 'PremiumSubscriptionOption'] = pydantic.Field(
        'types.PremiumSubscriptionOption',
        alias='_'
    )

    months: int
    currency: str
    amount: int
    bot_url: str
    current: typing.Optional[bool] = None
    can_purchase_upgrade: typing.Optional[bool] = None
    transaction: typing.Optional[str] = None
    store_product: typing.Optional[str] = None
