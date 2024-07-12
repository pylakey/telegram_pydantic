from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatlistUpdates(BaseModel):
    """
    types.chatlists.ChatlistUpdates
    ID: 0x93bd878d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.chatlists.ChatlistUpdates', 'ChatlistUpdates'] = pydantic.Field(
        'types.chatlists.ChatlistUpdates',
        alias='_'
    )

    missing_peers: list["base.Peer"]
    chats: list["base.Chat"]
    users: list["base.User"]
