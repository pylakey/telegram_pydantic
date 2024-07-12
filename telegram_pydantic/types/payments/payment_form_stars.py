from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PaymentFormStars(BaseModel):
    """
    types.payments.PaymentFormStars
    ID: 0x7bf6b15c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.PaymentFormStars', 'PaymentFormStars'] = pydantic.Field(
        'types.payments.PaymentFormStars',
        alias='_'
    )

    form_id: int
    bot_id: int
    title: str
    description: str
    invoice: "base.Invoice"
    users: list["base.User"]
    photo: typing.Optional["base.WebDocument"] = None
