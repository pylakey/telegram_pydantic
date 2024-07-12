from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MigrateChat(BaseModel):
    """
    functions.messages.MigrateChat
    ID: 0xa2875319
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.MigrateChat', 'MigrateChat'] = pydantic.Field(
        'functions.messages.MigrateChat',
        alias='_'
    )

    chat_id: int
