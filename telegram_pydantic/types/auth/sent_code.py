from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCode(BaseModel):
    """
    types.auth.SentCode
    ID: 0x5e002502
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCode', 'SentCode'] = pydantic.Field(
        'types.auth.SentCode',
        alias='_'
    )

    type: "base.auth.SentCodeType"
    phone_code_hash: str
    next_type: typing.Optional["base.auth.CodeType"] = None
    timeout: typing.Optional[int] = None
