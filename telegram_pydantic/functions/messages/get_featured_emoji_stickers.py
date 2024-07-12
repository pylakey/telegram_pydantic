from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetFeaturedEmojiStickers(BaseModel):
    """
    functions.messages.GetFeaturedEmojiStickers
    ID: 0xecf6736
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetFeaturedEmojiStickers', 'GetFeaturedEmojiStickers'] = pydantic.Field(
        'functions.messages.GetFeaturedEmojiStickers',
        alias='_'
    )

    hash: int
