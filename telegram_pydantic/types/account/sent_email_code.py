from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentEmailCode(BaseModel):
    """
    types.account.SentEmailCode
    ID: 0x811f854f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.SentEmailCode', 'SentEmailCode'] = pydantic.Field(
        'types.account.SentEmailCode',
        alias='_'
    )

    email_pattern: str
    length: int
