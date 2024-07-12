from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityUnderline(BaseModel):
    """
    types.MessageEntityUnderline
    ID: 0x9c4e7e8b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityUnderline', 'MessageEntityUnderline'] = pydantic.Field(
        'types.MessageEntityUnderline',
        alias='_'
    )

    offset: int
    length: int
