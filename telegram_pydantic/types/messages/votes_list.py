from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class VotesList(BaseModel):
    """
    types.messages.VotesList
    ID: 0x4899484e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.VotesList', 'VotesList'] = pydantic.Field(
        'types.messages.VotesList',
        alias='_'
    )

    count: int
    votes: list["base.MessagePeerVote"]
    chats: list["base.Chat"]
    users: list["base.User"]
    next_offset: typing.Optional[str] = None
