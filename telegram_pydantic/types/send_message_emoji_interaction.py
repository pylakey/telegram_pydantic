from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageEmojiInteraction(BaseModel):
    """
    types.SendMessageEmojiInteraction
    ID: 0x25972bcb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageEmojiInteraction', 'SendMessageEmojiInteraction'] = pydantic.Field(
        'types.SendMessageEmojiInteraction',
        alias='_'
    )

    emoticon: str
    msg_id: int
    interaction: "base.DataJSON"
