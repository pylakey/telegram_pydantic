from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChannelDefaultEmojiStatuses(BaseModel):
    """
    functions.account.GetChannelDefaultEmojiStatuses
    ID: 0x7727a7d5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetChannelDefaultEmojiStatuses', 'GetChannelDefaultEmojiStatuses'] = pydantic.Field(
        'functions.account.GetChannelDefaultEmojiStatuses',
        alias='_'
    )

    hash: int
