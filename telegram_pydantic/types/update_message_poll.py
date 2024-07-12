from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateMessagePoll(BaseModel):
    """
    types.UpdateMessagePoll
    ID: 0xaca1657b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateMessagePoll', 'UpdateMessagePoll'] = pydantic.Field(
        'types.UpdateMessagePoll',
        alias='_'
    )

    poll_id: int
    results: "base.PollResults"
    poll: typing.Optional["base.Poll"] = None
