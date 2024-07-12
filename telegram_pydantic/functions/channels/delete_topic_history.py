from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteTopicHistory(BaseModel):
    """
    functions.channels.DeleteTopicHistory
    ID: 0x34435f2d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.DeleteTopicHistory', 'DeleteTopicHistory'] = pydantic.Field(
        'functions.channels.DeleteTopicHistory',
        alias='_'
    )

    channel: "base.InputChannel"
    top_msg_id: int
