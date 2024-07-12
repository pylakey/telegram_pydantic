from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDiscussionMessage(BaseModel):
    """
    functions.messages.GetDiscussionMessage
    ID: 0x446972fd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDiscussionMessage', 'GetDiscussionMessage'] = pydantic.Field(
        'functions.messages.GetDiscussionMessage',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
