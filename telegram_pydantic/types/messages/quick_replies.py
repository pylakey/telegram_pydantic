from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class QuickReplies(BaseModel):
    """
    types.messages.QuickReplies
    ID: 0xc68d6695
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.QuickReplies', 'QuickReplies'] = pydantic.Field(
        'types.messages.QuickReplies',
        alias='_'
    )

    quick_replies: list["base.QuickReply"]
    messages: list["base.Message"]
    chats: list["base.Chat"]
    users: list["base.User"]
