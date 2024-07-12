from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResolvedBusinessChatLinks(BaseModel):
    """
    types.account.ResolvedBusinessChatLinks
    ID: 0x9a23af21
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.ResolvedBusinessChatLinks', 'ResolvedBusinessChatLinks'] = pydantic.Field(
        'types.account.ResolvedBusinessChatLinks',
        alias='_'
    )

    peer: "base.Peer"
    message: str
    chats: list["base.Chat"]
    users: list["base.User"]
    entities: typing.Optional[list["base.MessageEntity"]] = None
