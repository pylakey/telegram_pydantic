from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteScheduledMessages(BaseModel):
    """
    functions.messages.DeleteScheduledMessages
    ID: 0x59ae2b16
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteScheduledMessages', 'DeleteScheduledMessages'] = pydantic.Field(
        'functions.messages.DeleteScheduledMessages',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
