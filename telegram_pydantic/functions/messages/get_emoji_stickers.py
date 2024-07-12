from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetEmojiStickers(BaseModel):
    """
    functions.messages.GetEmojiStickers
    ID: 0xfbfca18f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetEmojiStickers', 'GetEmojiStickers'] = pydantic.Field(
        'functions.messages.GetEmojiStickers',
        alias='_'
    )

    hash: int
