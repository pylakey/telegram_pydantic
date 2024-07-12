from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentEncryptedFile(BaseModel):
    """
    types.messages.SentEncryptedFile
    ID: 0x9493ff32
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SentEncryptedFile', 'SentEncryptedFile'] = pydantic.Field(
        'types.messages.SentEncryptedFile',
        alias='_'
    )

    date: Datetime
    file: "base.EncryptedFile"
