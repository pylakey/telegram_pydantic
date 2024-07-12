from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class VerifyPhone(BaseModel):
    """
    functions.account.VerifyPhone
    ID: 0x4dd3a7f6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.VerifyPhone', 'VerifyPhone'] = pydantic.Field(
        'functions.account.VerifyPhone',
        alias='_'
    )

    phone_number: str
    phone_code_hash: str
    phone_code: str
