from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatlistInviteAlready(BaseModel):
    """
    types.chatlists.ChatlistInviteAlready
    ID: 0xfa87f659
    Layer: 181
    """
    QUALNAME: typing.Literal['types.chatlists.ChatlistInviteAlready', 'ChatlistInviteAlready'] = pydantic.Field(
        'types.chatlists.ChatlistInviteAlready',
        alias='_'
    )

    filter_id: int
    missing_peers: list["base.Peer"]
    already_peers: list["base.Peer"]
    chats: list["base.Chat"]
    users: list["base.User"]
