from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatlistInvite(BaseModel):
    """
    types.chatlists.ChatlistInvite
    ID: 0x1dcd839d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.chatlists.ChatlistInvite', 'ChatlistInvite'] = pydantic.Field(
        'types.chatlists.ChatlistInvite',
        alias='_'
    )

    title: str
    peers: list["base.Peer"]
    chats: list["base.Chat"]
    users: list["base.User"]
    emoticon: typing.Optional[str] = None
