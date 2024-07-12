from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PaymentReceipt(BaseModel):
    """
    types.payments.PaymentReceipt
    ID: 0x70c4fe03
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.PaymentReceipt', 'PaymentReceipt'] = pydantic.Field(
        'types.payments.PaymentReceipt',
        alias='_'
    )

    date: Datetime
    bot_id: int
    provider_id: int
    title: str
    description: str
    invoice: "base.Invoice"
    currency: str
    total_amount: int
    credentials_title: str
    users: list["base.User"]
    photo: typing.Optional["base.WebDocument"] = None
    info: typing.Optional["base.PaymentRequestedInfo"] = None
    shipping: typing.Optional["base.ShippingOption"] = None
    tip_amount: typing.Optional[int] = None
