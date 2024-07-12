from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetEmojiURL(BaseModel):
    """
    functions.messages.GetEmojiURL
    ID: 0xd5b10c26
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetEmojiURL', 'GetEmojiURL'] = pydantic.Field(
        'functions.messages.GetEmojiURL',
        alias='_'
    )

    lang_code: str
