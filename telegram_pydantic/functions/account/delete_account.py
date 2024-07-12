from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteAccount(BaseModel):
    """
    functions.account.DeleteAccount
    ID: 0xa2c0cf74
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.DeleteAccount', 'DeleteAccount'] = pydantic.Field(
        'functions.account.DeleteAccount',
        alias='_'
    )

    reason: str
    password: typing.Optional["base.InputCheckPasswordSRP"] = None
