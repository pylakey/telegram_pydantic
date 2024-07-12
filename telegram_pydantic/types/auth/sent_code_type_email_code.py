from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeEmailCode(BaseModel):
    """
    types.auth.SentCodeTypeEmailCode
    ID: 0xf450f59b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeEmailCode', 'SentCodeTypeEmailCode'] = pydantic.Field(
        'types.auth.SentCodeTypeEmailCode',
        alias='_'
    )

    email_pattern: str
    length: int
    apple_signin_allowed: typing.Optional[bool] = None
    google_signin_allowed: typing.Optional[bool] = None
    reset_available_period: typing.Optional[int] = None
    reset_pending_date: Datetime
