from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiKeyword(BaseModel):
    """
    types.EmojiKeyword
    ID: 0xd5b3b9f9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiKeyword', 'EmojiKeyword'] = pydantic.Field(
        'types.EmojiKeyword',
        alias='_'
    )

    keyword: str
    emoticons: list[str]
