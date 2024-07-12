from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Messages(BaseModel):
    """
    types.messages.Messages
    ID: 0x8c718e87
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.Messages', 'Messages'] = pydantic.Field(
        'types.messages.Messages',
        alias='_'
    )

    messages: list["base.Message"]
    chats: list["base.Chat"]
    users: list["base.User"]
