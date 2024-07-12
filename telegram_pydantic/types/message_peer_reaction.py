from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessagePeerReaction(BaseModel):
    """
    types.MessagePeerReaction
    ID: 0x8c79b63c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessagePeerReaction', 'MessagePeerReaction'] = pydantic.Field(
        'types.MessagePeerReaction',
        alias='_'
    )

    peer_id: "base.Peer"
    date: Datetime
    reaction: "base.Reaction"
    big: typing.Optional[bool] = None
    unread: typing.Optional[bool] = None
    my: typing.Optional[bool] = None
