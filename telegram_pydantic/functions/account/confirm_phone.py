from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ConfirmPhone(BaseModel):
    """
    functions.account.ConfirmPhone
    ID: 0x5f2178c3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ConfirmPhone', 'ConfirmPhone'] = pydantic.Field(
        'functions.account.ConfirmPhone',
        alias='_'
    )

    phone_code_hash: str
    phone_code: str
