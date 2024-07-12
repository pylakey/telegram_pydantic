from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchEmojiStickerSets(BaseModel):
    """
    functions.messages.SearchEmojiStickerSets
    ID: 0x92b4494c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SearchEmojiStickerSets', 'SearchEmojiStickerSets'] = pydantic.Field(
        'functions.messages.SearchEmojiStickerSets',
        alias='_'
    )

    q: str
    hash: int
    exclude_featured: typing.Optional[bool] = None
