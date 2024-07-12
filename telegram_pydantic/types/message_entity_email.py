from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityEmail(BaseModel):
    """
    types.MessageEntityEmail
    ID: 0x64e475c2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityEmail', 'MessageEntityEmail'] = pydantic.Field(
        'types.MessageEntityEmail',
        alias='_'
    )

    offset: int
    length: int
