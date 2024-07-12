from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityItalic(BaseModel):
    """
    types.MessageEntityItalic
    ID: 0x826f8b60
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityItalic', 'MessageEntityItalic'] = pydantic.Field(
        'types.MessageEntityItalic',
        alias='_'
    )

    offset: int
    length: int
