from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendVerifyEmailCode(BaseModel):
    """
    functions.account.SendVerifyEmailCode
    ID: 0x98e037bb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SendVerifyEmailCode', 'SendVerifyEmailCode'] = pydantic.Field(
        'functions.account.SendVerifyEmailCode',
        alias='_'
    )

    purpose: "base.EmailVerifyPurpose"
    email: str
