from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityCustomEmoji(BaseModel):
    """
    types.MessageEntityCustomEmoji
    ID: 0xc8cf05f8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityCustomEmoji', 'MessageEntityCustomEmoji'] = pydantic.Field(
        'types.MessageEntityCustomEmoji',
        alias='_'
    )

    offset: int
    length: int
    document_id: int
