from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchCustomEmoji(BaseModel):
    """
    functions.messages.SearchCustomEmoji
    ID: 0x2c11c0d7
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SearchCustomEmoji', 'SearchCustomEmoji'] = pydantic.Field(
        'functions.messages.SearchCustomEmoji',
        alias='_'
    )

    emoticon: str
    hash: int
