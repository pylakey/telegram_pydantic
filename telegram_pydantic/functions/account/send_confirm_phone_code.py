from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendConfirmPhoneCode(BaseModel):
    """
    functions.account.SendConfirmPhoneCode
    ID: 0x1b3faa88
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SendConfirmPhoneCode', 'SendConfirmPhoneCode'] = pydantic.Field(
        'functions.account.SendConfirmPhoneCode',
        alias='_'
    )

    hash: str
    settings: "base.CodeSettings"
