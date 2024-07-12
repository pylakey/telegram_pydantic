from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageReactionsList(BaseModel):
    """
    types.messages.MessageReactionsList
    ID: 0x31bd492d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.MessageReactionsList', 'MessageReactionsList'] = pydantic.Field(
        'types.messages.MessageReactionsList',
        alias='_'
    )

    count: int
    reactions: list["base.MessagePeerReaction"]
    chats: list["base.Chat"]
    users: list["base.User"]
    next_offset: typing.Optional[str] = None
