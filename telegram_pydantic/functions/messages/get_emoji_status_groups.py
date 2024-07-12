from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetEmojiStatusGroups(BaseModel):
    """
    functions.messages.GetEmojiStatusGroups
    ID: 0x2ecd56cd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetEmojiStatusGroups', 'GetEmojiStatusGroups'] = pydantic.Field(
        'functions.messages.GetEmojiStatusGroups',
        alias='_'
    )

    hash: int
