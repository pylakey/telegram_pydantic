from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatFull(BaseModel):
    """
    types.messages.ChatFull
    ID: 0xe5d7d19c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ChatFull', 'ChatFull'] = pydantic.Field(
        'types.messages.ChatFull',
        alias='_'
    )

    full_chat: "base.ChatFull"
    chats: list["base.Chat"]
    users: list["base.User"]
