from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReplyToMessage(BaseModel):
    """
    types.InputReplyToMessage
    ID: 0x22c0f6d5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReplyToMessage', 'InputReplyToMessage'] = pydantic.Field(
        'types.InputReplyToMessage',
        alias='_'
    )

    reply_to_msg_id: int
    top_msg_id: typing.Optional[int] = None
    reply_to_peer_id: typing.Optional["base.InputPeer"] = None
    quote_text: typing.Optional[str] = None
    quote_entities: typing.Optional[list["base.MessageEntity"]] = None
    quote_offset: typing.Optional[int] = None
