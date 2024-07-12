from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PaymentCharge(BaseModel):
    """
    types.PaymentCharge
    ID: 0xea02c27e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PaymentCharge', 'PaymentCharge'] = pydantic.Field(
        'types.PaymentCharge',
        alias='_'
    )

    id: str
    provider_charge_id: str
