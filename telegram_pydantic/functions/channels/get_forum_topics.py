from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetForumTopics(BaseModel):
    """
    functions.channels.GetForumTopics
    ID: 0xde560d1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetForumTopics', 'GetForumTopics'] = pydantic.Field(
        'functions.channels.GetForumTopics',
        alias='_'
    )

    channel: "base.InputChannel"
    offset_date: Datetime
    offset_id: int
    offset_topic: int
    limit: int
    q: typing.Optional[str] = None
