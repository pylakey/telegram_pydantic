from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedChatWaiting(BaseModel):
    """
    types.EncryptedChatWaiting
    ID: 0x66b25953
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedChatWaiting', 'EncryptedChatWaiting'] = pydantic.Field(
        'types.EncryptedChatWaiting',
        alias='_'
    )

    id: int
    access_hash: int
    date: Datetime
    admin_id: int
    participant_id: int
