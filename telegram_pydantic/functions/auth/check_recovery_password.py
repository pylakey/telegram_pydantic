from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckRecoveryPassword(BaseModel):
    """
    functions.auth.CheckRecoveryPassword
    ID: 0xd36bf79
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.CheckRecoveryPassword', 'CheckRecoveryPassword'] = pydantic.Field(
        'functions.auth.CheckRecoveryPassword',
        alias='_'
    )

    code: str
