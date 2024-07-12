from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResendCode(BaseModel):
    """
    functions.auth.ResendCode
    ID: 0xcae47523
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.ResendCode', 'ResendCode'] = pydantic.Field(
        'functions.auth.ResendCode',
        alias='_'
    )

    phone_number: str
    phone_code_hash: str
    reason: typing.Optional[str] = None
