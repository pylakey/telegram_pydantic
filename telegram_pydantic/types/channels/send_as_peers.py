from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendAsPeers(BaseModel):
    """
    types.channels.SendAsPeers
    ID: 0xf496b0c6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.channels.SendAsPeers', 'SendAsPeers'] = pydantic.Field(
        'types.channels.SendAsPeers',
        alias='_'
    )

    peers: list["base.SendAsPeer"]
    chats: list["base.Chat"]
    users: list["base.User"]
