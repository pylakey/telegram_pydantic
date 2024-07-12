from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPaymentCredentialsApplePay(BaseModel):
    """
    types.InputPaymentCredentialsApplePay
    ID: 0xaa1c39f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPaymentCredentialsApplePay', 'InputPaymentCredentialsApplePay'] = pydantic.Field(
        'types.InputPaymentCredentialsApplePay',
        alias='_'
    )

    payment_data: "base.DataJSON"
