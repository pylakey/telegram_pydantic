from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateEmojiStatus(BaseModel):
    """
    functions.account.UpdateEmojiStatus
    ID: 0xfbd3de6b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateEmojiStatus', 'UpdateEmojiStatus'] = pydantic.Field(
        'functions.account.UpdateEmojiStatus',
        alias='_'
    )

    emoji_status: "base.EmojiStatus"
