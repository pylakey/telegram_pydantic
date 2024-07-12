from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessagePeerVote(BaseModel):
    """
    types.MessagePeerVote
    ID: 0xb6cc2d5c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessagePeerVote', 'MessagePeerVote'] = pydantic.Field(
        'types.MessagePeerVote',
        alias='_'
    )

    peer: "base.Peer"
    option: Bytes
    date: Datetime
