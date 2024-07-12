from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaPoll(BaseModel):
    """
    types.MessageMediaPoll
    ID: 0x4bd6e798
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaPoll', 'MessageMediaPoll'] = pydantic.Field(
        'types.MessageMediaPoll',
        alias='_'
    )

    poll: "base.Poll"
    results: "base.PollResults"
