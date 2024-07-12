from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmailVerificationCode(BaseModel):
    """
    types.EmailVerificationCode
    ID: 0x922e55a9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmailVerificationCode', 'EmailVerificationCode'] = pydantic.Field(
        'types.EmailVerificationCode',
        alias='_'
    )

    code: str
