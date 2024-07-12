from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Updates(BaseModel):
    """
    types.Updates
    ID: 0x74ae4240
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Updates', 'Updates'] = pydantic.Field(
        'types.Updates',
        alias='_'
    )

    updates: list["base.Update"]
    users: list["base.User"]
    chats: list["base.Chat"]
    date: Datetime
    seq: int
