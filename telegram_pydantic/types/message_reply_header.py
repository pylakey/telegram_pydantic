from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageReplyHeader(BaseModel):
    """
    types.MessageReplyHeader
    ID: 0xafbc09db
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageReplyHeader', 'MessageReplyHeader'] = pydantic.Field(
        'types.MessageReplyHeader',
        alias='_'
    )

    reply_to_scheduled: typing.Optional[bool] = None
    forum_topic: typing.Optional[bool] = None
    quote: typing.Optional[bool] = None
    reply_to_msg_id: typing.Optional[int] = None
    reply_to_peer_id: typing.Optional["base.Peer"] = None
    reply_from: typing.Optional["base.MessageFwdHeader"] = None
    reply_media: typing.Optional["base.MessageMedia"] = None
    reply_to_top_id: typing.Optional[int] = None
    quote_text: typing.Optional[str] = None
    quote_entities: typing.Optional[list["base.MessageEntity"]] = None
    quote_offset: typing.Optional[int] = None
