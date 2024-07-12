from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PaymentVerificationNeeded(BaseModel):
    """
    types.payments.PaymentVerificationNeeded
    ID: 0xd8411139
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.PaymentVerificationNeeded', 'PaymentVerificationNeeded'] = pydantic.Field(
        'types.payments.PaymentVerificationNeeded',
        alias='_'
    )

    url: str
