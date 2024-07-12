from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CanPurchasePremium(BaseModel):
    """
    functions.payments.CanPurchasePremium
    ID: 0x9fc19eb6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.CanPurchasePremium', 'CanPurchasePremium'] = pydantic.Field(
        'functions.payments.CanPurchasePremium',
        alias='_'
    )

    purpose: "base.InputStorePaymentPurpose"
