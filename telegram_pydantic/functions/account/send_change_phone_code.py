from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendChangePhoneCode(BaseModel):
    """
    functions.account.SendChangePhoneCode
    ID: 0x82574ae5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SendChangePhoneCode', 'SendChangePhoneCode'] = pydantic.Field(
        'functions.account.SendChangePhoneCode',
        alias='_'
    )

    phone_number: str
    settings: "base.CodeSettings"
