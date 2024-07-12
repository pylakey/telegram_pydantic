from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatForbidden(BaseModel):
    """
    types.ChatForbidden
    ID: 0x6592a1a7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatForbidden', 'ChatForbidden'] = pydantic.Field(
        'types.ChatForbidden',
        alias='_'
    )

    id: int
    title: str
