from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDefaultEmojiStatuses(BaseModel):
    """
    functions.account.GetDefaultEmojiStatuses
    ID: 0xd6753386
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetDefaultEmojiStatuses', 'GetDefaultEmojiStatuses'] = pydantic.Field(
        'functions.account.GetDefaultEmojiStatuses',
        alias='_'
    )

    hash: int
