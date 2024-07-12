from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentEncryptedMessage(BaseModel):
    """
    types.messages.SentEncryptedMessage
    ID: 0x560f8935
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SentEncryptedMessage', 'SentEncryptedMessage'] = pydantic.Field(
        'types.messages.SentEncryptedMessage',
        alias='_'
    )

    date: Datetime
