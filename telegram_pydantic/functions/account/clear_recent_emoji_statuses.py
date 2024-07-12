from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ClearRecentEmojiStatuses(BaseModel):
    """
    functions.account.ClearRecentEmojiStatuses
    ID: 0x18201aae
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ClearRecentEmojiStatuses', 'ClearRecentEmojiStatuses'] = pydantic.Field(
        'functions.account.ClearRecentEmojiStatuses',
        alias='_'
    )

