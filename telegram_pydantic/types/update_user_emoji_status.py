from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateUserEmojiStatus(BaseModel):
    """
    types.UpdateUserEmojiStatus
    ID: 0x28373599
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateUserEmojiStatus', 'UpdateUserEmojiStatus'] = pydantic.Field(
        'types.UpdateUserEmojiStatus',
        alias='_'
    )

    user_id: int
    emoji_status: "base.EmojiStatus"
