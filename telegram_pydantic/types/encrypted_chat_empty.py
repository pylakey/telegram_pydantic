from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedChatEmpty(BaseModel):
    """
    types.EncryptedChatEmpty
    ID: 0xab7ec0a0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedChatEmpty', 'EncryptedChatEmpty'] = pydantic.Field(
        'types.EncryptedChatEmpty',
        alias='_'
    )

    id: int
