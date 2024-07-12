from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendScheduledMessages(BaseModel):
    """
    functions.messages.SendScheduledMessages
    ID: 0xbd38850a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendScheduledMessages', 'SendScheduledMessages'] = pydantic.Field(
        'functions.messages.SendScheduledMessages',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
