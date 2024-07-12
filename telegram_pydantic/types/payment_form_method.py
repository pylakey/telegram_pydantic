from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PaymentFormMethod(BaseModel):
    """
    types.PaymentFormMethod
    ID: 0x88f8f21b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PaymentFormMethod', 'PaymentFormMethod'] = pydantic.Field(
        'types.PaymentFormMethod',
        alias='_'
    )

    url: str
    title: str
