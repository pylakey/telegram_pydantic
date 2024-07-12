from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CancelCode(BaseModel):
    """
    functions.auth.CancelCode
    ID: 0x1f040578
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.CancelCode', 'CancelCode'] = pydantic.Field(
        'functions.auth.CancelCode',
        alias='_'
    )

    phone_number: str
    phone_code_hash: str
