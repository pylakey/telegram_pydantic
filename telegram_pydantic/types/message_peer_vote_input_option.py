from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessagePeerVoteInputOption(BaseModel):
    """
    types.MessagePeerVoteInputOption
    ID: 0x74cda504
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessagePeerVoteInputOption', 'MessagePeerVoteInputOption'] = pydantic.Field(
        'types.MessagePeerVoteInputOption',
        alias='_'
    )

    peer: "base.Peer"
    date: Datetime
