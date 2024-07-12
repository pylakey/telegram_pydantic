from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionPaymentSentMe(BaseModel):
    """
    types.MessageActionPaymentSentMe
    ID: 0x8f31b327
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionPaymentSentMe', 'MessageActionPaymentSentMe'] = pydantic.Field(
        'types.MessageActionPaymentSentMe',
        alias='_'
    )

    currency: str
    total_amount: int
    payload: Bytes
    charge: "base.PaymentCharge"
    recurring_init: typing.Optional[bool] = None
    recurring_used: typing.Optional[bool] = None
    info: typing.Optional["base.PaymentRequestedInfo"] = None
    shipping_option_id: typing.Optional[str] = None
