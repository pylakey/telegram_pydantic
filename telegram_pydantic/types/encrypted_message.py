from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedMessage(BaseModel):
    """
    types.EncryptedMessage
    ID: 0xed18c118
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedMessage', 'EncryptedMessage'] = pydantic.Field(
        'types.EncryptedMessage',
        alias='_'
    )

    random_id: int
    chat_id: int
    date: Datetime
    bytes: Bytes
    file: "base.EncryptedFile"
