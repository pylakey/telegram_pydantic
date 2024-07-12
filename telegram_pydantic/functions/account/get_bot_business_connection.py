from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBotBusinessConnection(BaseModel):
    """
    functions.account.GetBotBusinessConnection
    ID: 0x76a86270
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetBotBusinessConnection', 'GetBotBusinessConnection'] = pydantic.Field(
        'functions.account.GetBotBusinessConnection',
        alias='_'
    )

    connection_id: str
