from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPaymentForm(BaseModel):
    """
    functions.payments.GetPaymentForm
    ID: 0x37148dbb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.GetPaymentForm', 'GetPaymentForm'] = pydantic.Field(
        'functions.payments.GetPaymentForm',
        alias='_'
    )

    invoice: "base.InputInvoice"
    theme_params: typing.Optional["base.DataJSON"] = None
