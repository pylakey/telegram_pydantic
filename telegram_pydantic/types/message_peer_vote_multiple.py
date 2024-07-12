from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessagePeerVoteMultiple(BaseModel):
    """
    types.MessagePeerVoteMultiple
    ID: 0x4628f6e6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessagePeerVoteMultiple', 'MessagePeerVoteMultiple'] = pydantic.Field(
        'types.MessagePeerVoteMultiple',
        alias='_'
    )

    peer: "base.Peer"
    options: list[Bytes]
    date: Datetime
