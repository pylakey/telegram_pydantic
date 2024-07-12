from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiGroupGreeting(BaseModel):
    """
    types.EmojiGroupGreeting
    ID: 0x80d26cc7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiGroupGreeting', 'EmojiGroupGreeting'] = pydantic.Field(
        'types.EmojiGroupGreeting',
        alias='_'
    )

    title: str
    icon_emoji_id: int
    emoticons: list[str]
