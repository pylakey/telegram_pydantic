from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DiscussionMessage(BaseModel):
    """
    types.messages.DiscussionMessage
    ID: 0xa6341782
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.DiscussionMessage', 'DiscussionMessage'] = pydantic.Field(
        'types.messages.DiscussionMessage',
        alias='_'
    )

    messages: list["base.Message"]
    unread_count: int
    chats: list["base.Chat"]
    users: list["base.User"]
    max_id: typing.Optional[int] = None
    read_inbox_max_id: typing.Optional[int] = None
    read_outbox_max_id: typing.Optional[int] = None
