from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedChatRequested(BaseModel):
    """
    types.EncryptedChatRequested
    ID: 0x48f1d94c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedChatRequested', 'EncryptedChatRequested'] = pydantic.Field(
        'types.EncryptedChatRequested',
        alias='_'
    )

    id: int
    access_hash: int
    date: Datetime
    admin_id: int
    participant_id: int
    g_a: Bytes
    folder_id: typing.Optional[int] = None
