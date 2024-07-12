from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InactiveChats(BaseModel):
    """
    types.messages.InactiveChats
    ID: 0xa927fec5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.InactiveChats', 'InactiveChats'] = pydantic.Field(
        'types.messages.InactiveChats',
        alias='_'
    )

    dates: list[int]
    chats: list["base.Chat"]
    users: list["base.User"]
