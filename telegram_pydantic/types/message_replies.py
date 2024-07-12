from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageReplies(BaseModel):
    """
    types.MessageReplies
    ID: 0x83d60fc2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageReplies', 'MessageReplies'] = pydantic.Field(
        'types.MessageReplies',
        alias='_'
    )

    replies: int
    replies_pts: int
    comments: typing.Optional[bool] = None
    recent_repliers: typing.Optional[list["base.Peer"]] = None
    channel_id: typing.Optional[int] = None
    max_id: typing.Optional[int] = None
    read_max_id: typing.Optional[int] = None
