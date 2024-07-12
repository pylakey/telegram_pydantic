from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotBusinessConnection(BaseModel):
    """
    types.BotBusinessConnection
    ID: 0x896433b4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotBusinessConnection', 'BotBusinessConnection'] = pydantic.Field(
        'types.BotBusinessConnection',
        alias='_'
    )

    connection_id: str
    user_id: int
    dc_id: int
    date: Datetime
    can_reply: typing.Optional[bool] = None
    disabled: typing.Optional[bool] = None
