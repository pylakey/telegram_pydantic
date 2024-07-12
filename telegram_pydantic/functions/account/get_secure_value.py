from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSecureValue(BaseModel):
    """
    functions.account.GetSecureValue
    ID: 0x73665bc2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetSecureValue', 'GetSecureValue'] = pydantic.Field(
        'functions.account.GetSecureValue',
        alias='_'
    )

    types: list["base.SecureValueType"]
