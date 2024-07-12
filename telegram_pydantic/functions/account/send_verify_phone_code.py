from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendVerifyPhoneCode(BaseModel):
    """
    functions.account.SendVerifyPhoneCode
    ID: 0xa5a356f9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SendVerifyPhoneCode', 'SendVerifyPhoneCode'] = pydantic.Field(
        'functions.account.SendVerifyPhoneCode',
        alias='_'
    )

    phone_number: str
    settings: "base.CodeSettings"
