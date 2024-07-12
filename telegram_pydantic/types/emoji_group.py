from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiGroup(BaseModel):
    """
    types.EmojiGroup
    ID: 0x7a9abda9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiGroup', 'EmojiGroup'] = pydantic.Field(
        'types.EmojiGroup',
        alias='_'
    )

    title: str
    icon_emoji_id: int
    emoticons: list[str]
