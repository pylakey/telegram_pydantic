from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPollVotes(BaseModel):
    """
    functions.messages.GetPollVotes
    ID: 0xb86e380e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetPollVotes', 'GetPollVotes'] = pydantic.Field(
        'functions.messages.GetPollVotes',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
    limit: int
    option: typing.Optional[Bytes] = None
    offset: typing.Optional[str] = None
