from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipant(BaseModel):
    """
    types.channels.ChannelParticipant
    ID: 0xdfb80317
    Layer: 181
    """
    QUALNAME: typing.Literal['types.channels.ChannelParticipant', 'ChannelParticipant'] = pydantic.Field(
        'types.channels.ChannelParticipant',
        alias='_'
    )

    participant: "base.ChannelParticipant"
    chats: list["base.Chat"]
    users: list["base.User"]
