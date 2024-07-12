from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateMessagePollVote(BaseModel):
    """
    types.UpdateMessagePollVote
    ID: 0x24f40e77
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateMessagePollVote', 'UpdateMessagePollVote'] = pydantic.Field(
        'types.UpdateMessagePollVote',
        alias='_'
    )

    poll_id: int
    peer: "base.Peer"
    options: list[Bytes]
    qts: int
