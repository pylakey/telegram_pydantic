from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelMessages(BaseModel):
    """
    types.messages.ChannelMessages
    ID: 0xc776ba4e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ChannelMessages', 'ChannelMessages'] = pydantic.Field(
        'types.messages.ChannelMessages',
        alias='_'
    )

    pts: int
    count: int
    messages: list["base.Message"]
    topics: list["base.ForumTopic"]
    chats: list["base.Chat"]
    users: list["base.User"]
    inexact: typing.Optional[bool] = None
    offset_id_offset: typing.Optional[int] = None
