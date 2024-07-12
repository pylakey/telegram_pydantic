from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Chats(BaseModel):
    """
    types.messages.Chats
    ID: 0x64ff9fd5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.Chats', 'Chats'] = pydantic.Field(
        'types.messages.Chats',
        alias='_'
    )

    chats: list["base.Chat"]
