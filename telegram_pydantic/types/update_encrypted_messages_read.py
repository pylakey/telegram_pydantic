from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateEncryptedMessagesRead(BaseModel):
    """
    types.UpdateEncryptedMessagesRead
    ID: 0x38fe25b7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateEncryptedMessagesRead', 'UpdateEncryptedMessagesRead'] = pydantic.Field(
        'types.UpdateEncryptedMessagesRead',
        alias='_'
    )

    chat_id: int
    max_date: Datetime
    date: Datetime
