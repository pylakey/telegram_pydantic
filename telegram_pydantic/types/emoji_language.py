from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiLanguage(BaseModel):
    """
    types.EmojiLanguage
    ID: 0xb3fb5361
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiLanguage', 'EmojiLanguage'] = pydantic.Field(
        'types.EmojiLanguage',
        alias='_'
    )

    lang_code: str
