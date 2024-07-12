from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPassword(BaseModel):
    """
    functions.account.GetPassword
    ID: 0x548a30f5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetPassword', 'GetPassword'] = pydantic.Field(
        'functions.account.GetPassword',
        alias='_'
    )

