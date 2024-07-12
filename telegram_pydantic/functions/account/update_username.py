from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateUsername(BaseModel):
    """
    functions.account.UpdateUsername
    ID: 0x3e0bdd7c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateUsername', 'UpdateUsername'] = pydantic.Field(
        'functions.account.UpdateUsername',
        alias='_'
    )

    username: str
