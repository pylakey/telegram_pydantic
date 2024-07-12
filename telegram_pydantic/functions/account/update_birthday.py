from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBirthday(BaseModel):
    """
    functions.account.UpdateBirthday
    ID: 0xcc6e0c11
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateBirthday', 'UpdateBirthday'] = pydantic.Field(
        'functions.account.UpdateBirthday',
        alias='_'
    )

    birthday: typing.Optional["base.Birthday"] = None
