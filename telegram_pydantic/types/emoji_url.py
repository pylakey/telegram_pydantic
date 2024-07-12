from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiURL(BaseModel):
    """
    types.EmojiURL
    ID: 0xa575739d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiURL', 'EmojiURL'] = pydantic.Field(
        'types.EmojiURL',
        alias='_'
    )

    url: str
