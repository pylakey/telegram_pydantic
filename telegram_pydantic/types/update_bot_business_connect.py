from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotBusinessConnect(BaseModel):
    """
    types.UpdateBotBusinessConnect
    ID: 0x8ae5c97a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotBusinessConnect', 'UpdateBotBusinessConnect'] = pydantic.Field(
        'types.UpdateBotBusinessConnect',
        alias='_'
    )

    connection: "base.BotBusinessConnection"
    qts: int
