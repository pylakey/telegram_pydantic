from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetEmojiKeywords(BaseModel):
    """
    functions.messages.GetEmojiKeywords
    ID: 0x35a0e062
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetEmojiKeywords', 'GetEmojiKeywords'] = pydantic.Field(
        'functions.messages.GetEmojiKeywords',
        alias='_'
    )

    lang_code: str
