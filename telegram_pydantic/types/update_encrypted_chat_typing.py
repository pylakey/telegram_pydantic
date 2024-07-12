from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateEncryptedChatTyping(BaseModel):
    """
    types.UpdateEncryptedChatTyping
    ID: 0x1710f156
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateEncryptedChatTyping', 'UpdateEncryptedChatTyping'] = pydantic.Field(
        'types.UpdateEncryptedChatTyping',
        alias='_'
    )

    chat_id: int
