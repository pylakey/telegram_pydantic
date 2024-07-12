from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedMessageService(BaseModel):
    """
    types.EncryptedMessageService
    ID: 0x23734b06
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedMessageService', 'EncryptedMessageService'] = pydantic.Field(
        'types.EncryptedMessageService',
        alias='_'
    )

    random_id: int
    chat_id: int
    date: Datetime
    bytes: Bytes
