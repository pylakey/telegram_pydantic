from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipants(BaseModel):
    """
    types.channels.ChannelParticipants
    ID: 0x9ab0feaf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.channels.ChannelParticipants', 'ChannelParticipants'] = pydantic.Field(
        'types.channels.ChannelParticipants',
        alias='_'
    )

    count: int
    participants: list["base.ChannelParticipant"]
    chats: list["base.Chat"]
    users: list["base.User"]
