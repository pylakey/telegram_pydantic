from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetForumTopicsByID(BaseModel):
    """
    functions.channels.GetForumTopicsByID
    ID: 0xb0831eb9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetForumTopicsByID', 'GetForumTopicsByID'] = pydantic.Field(
        'functions.channels.GetForumTopicsByID',
        alias='_'
    )

    channel: "base.InputChannel"
    topics: list[int]
