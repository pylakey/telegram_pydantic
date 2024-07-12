from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPaymentCredentialsGooglePay(BaseModel):
    """
    types.InputPaymentCredentialsGooglePay
    ID: 0x8ac32801
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPaymentCredentialsGooglePay', 'InputPaymentCredentialsGooglePay'] = pydantic.Field(
        'types.InputPaymentCredentialsGooglePay',
        alias='_'
    )

    payment_token: "base.DataJSON"
