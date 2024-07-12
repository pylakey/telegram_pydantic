from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStorePaymentGiftPremium(BaseModel):
    """
    types.InputStorePaymentGiftPremium
    ID: 0x616f7fe8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStorePaymentGiftPremium', 'InputStorePaymentGiftPremium'] = pydantic.Field(
        'types.InputStorePaymentGiftPremium',
        alias='_'
    )

    user_id: "base.InputUser"
    currency: str
    amount: int
