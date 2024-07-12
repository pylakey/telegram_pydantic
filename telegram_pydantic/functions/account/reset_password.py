from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetPassword(BaseModel):
    """
    functions.account.ResetPassword
    ID: 0x9308ce1b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ResetPassword', 'ResetPassword'] = pydantic.Field(
        'functions.account.ResetPassword',
        alias='_'
    )

