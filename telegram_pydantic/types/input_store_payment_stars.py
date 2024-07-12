from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStorePaymentStars(BaseModel):
    """
    types.InputStorePaymentStars
    ID: 0x4f0ee8df
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStorePaymentStars', 'InputStorePaymentStars'] = pydantic.Field(
        'types.InputStorePaymentStars',
        alias='_'
    )

    stars: int
    currency: str
    amount: int
