from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendCode(BaseModel):
    """
    functions.auth.SendCode
    ID: 0xa677244f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.SendCode', 'SendCode'] = pydantic.Field(
        'functions.auth.SendCode',
        alias='_'
    )

    phone_number: str
    api_id: int
    api_hash: str
    settings: "base.CodeSettings"
