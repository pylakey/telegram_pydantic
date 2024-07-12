from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDeleteScheduledMessages(BaseModel):
    """
    types.UpdateDeleteScheduledMessages
    ID: 0x90866cee
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDeleteScheduledMessages', 'UpdateDeleteScheduledMessages'] = pydantic.Field(
        'types.UpdateDeleteScheduledMessages',
        alias='_'
    )

    peer: "base.Peer"
    messages: list[int]
