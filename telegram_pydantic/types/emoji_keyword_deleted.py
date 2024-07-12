from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiKeywordDeleted(BaseModel):
    """
    types.EmojiKeywordDeleted
    ID: 0x236df622
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiKeywordDeleted', 'EmojiKeywordDeleted'] = pydantic.Field(
        'types.EmojiKeywordDeleted',
        alias='_'
    )

    keyword: str
    emoticons: list[str]
