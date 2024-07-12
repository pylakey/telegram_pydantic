from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendPaymentForm(BaseModel):
    """
    functions.payments.SendPaymentForm
    ID: 0x2d03522f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.SendPaymentForm', 'SendPaymentForm'] = pydantic.Field(
        'functions.payments.SendPaymentForm',
        alias='_'
    )

    form_id: int
    invoice: "base.InputInvoice"
    credentials: "base.InputPaymentCredentials"
    requested_info_id: typing.Optional[str] = None
    shipping_option_id: typing.Optional[str] = None
    tip_amount: typing.Optional[int] = None
