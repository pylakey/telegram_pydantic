from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DiscardEncryption(BaseModel):
    """
    functions.messages.DiscardEncryption
    ID: 0xf393aea0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DiscardEncryption', 'DiscardEncryption'] = pydantic.Field(
        'functions.messages.DiscardEncryption',
        alias='_'
    )

    chat_id: int
    delete_history: typing.Optional[bool] = None
