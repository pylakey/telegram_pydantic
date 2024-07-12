from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetFullChat(BaseModel):
    """
    functions.messages.GetFullChat
    ID: 0xaeb00b34
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetFullChat', 'GetFullChat'] = pydantic.Field(
        'functions.messages.GetFullChat',
        alias='_'
    )

    chat_id: int
