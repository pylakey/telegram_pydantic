from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PaymentReceiptStars(BaseModel):
    """
    types.payments.PaymentReceiptStars
    ID: 0xdabbf83a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.PaymentReceiptStars', 'PaymentReceiptStars'] = pydantic.Field(
        'types.payments.PaymentReceiptStars',
        alias='_'
    )

    date: Datetime
    bot_id: int
    title: str
    description: str
    invoice: "base.Invoice"
    currency: str
    total_amount: int
    transaction_id: str
    users: list["base.User"]
    photo: typing.Optional["base.WebDocument"] = None
