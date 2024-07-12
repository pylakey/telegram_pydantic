from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CreateChat(BaseModel):
    """
    functions.messages.CreateChat
    ID: 0x92ceddd4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.CreateChat', 'CreateChat'] = pydantic.Field(
        'functions.messages.CreateChat',
        alias='_'
    )

    users: list["base.InputUser"]
    title: str
    ttl_period: typing.Optional[int] = None
