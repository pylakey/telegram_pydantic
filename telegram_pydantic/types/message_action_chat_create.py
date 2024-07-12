from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChatCreate(BaseModel):
    """
    types.MessageActionChatCreate
    ID: 0xbd47cbad
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChatCreate', 'MessageActionChatCreate'] = pydantic.Field(
        'types.MessageActionChatCreate',
        alias='_'
    )

    title: str
    users: list[int]
