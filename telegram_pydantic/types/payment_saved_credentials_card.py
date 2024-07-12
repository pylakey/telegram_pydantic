from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PaymentSavedCredentialsCard(BaseModel):
    """
    types.PaymentSavedCredentialsCard
    ID: 0xcdc27a1f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PaymentSavedCredentialsCard', 'PaymentSavedCredentialsCard'] = pydantic.Field(
        'types.PaymentSavedCredentialsCard',
        alias='_'
    )

    id: str
    title: str
