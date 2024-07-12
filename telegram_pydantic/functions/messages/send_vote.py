from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendVote(BaseModel):
    """
    functions.messages.SendVote
    ID: 0x10ea6184
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendVote', 'SendVote'] = pydantic.Field(
        'functions.messages.SendVote',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    options: list[Bytes]
