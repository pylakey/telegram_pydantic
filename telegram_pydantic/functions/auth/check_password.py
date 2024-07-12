from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckPassword(BaseModel):
    """
    functions.auth.CheckPassword
    ID: 0xd18b4d16
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.CheckPassword', 'CheckPassword'] = pydantic.Field(
        'functions.auth.CheckPassword',
        alias='_'
    )

    password: "base.InputCheckPasswordSRP"
