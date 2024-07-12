from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveSecureValue(BaseModel):
    """
    functions.account.SaveSecureValue
    ID: 0x899fe31d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SaveSecureValue', 'SaveSecureValue'] = pydantic.Field(
        'functions.account.SaveSecureValue',
        alias='_'
    )

    value: "base.InputSecureValue"
    secure_secret_id: int
