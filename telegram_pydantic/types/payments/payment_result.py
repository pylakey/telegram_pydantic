from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PaymentResult(BaseModel):
    """
    types.payments.PaymentResult
    ID: 0x4e5f810d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.PaymentResult', 'PaymentResult'] = pydantic.Field(
        'types.payments.PaymentResult',
        alias='_'
    )

    updates: "base.Updates"
