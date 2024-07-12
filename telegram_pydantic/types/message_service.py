from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageService(BaseModel):
    """
    types.MessageService
    ID: 0x2b085862
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageService', 'MessageService'] = pydantic.Field(
        'types.MessageService',
        alias='_'
    )

    id: int
    peer_id: "base.Peer"
    date: Datetime
    action: "base.MessageAction"
    out: typing.Optional[bool] = None
    mentioned: typing.Optional[bool] = None
    media_unread: typing.Optional[bool] = None
    silent: typing.Optional[bool] = None
    post: typing.Optional[bool] = None
    legacy: typing.Optional[bool] = None
    from_id: typing.Optional["base.Peer"] = None
    reply_to: typing.Optional["base.MessageReplyHeader"] = None
    ttl_period: typing.Optional[int] = None
