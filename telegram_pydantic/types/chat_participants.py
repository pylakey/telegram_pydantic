from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatParticipants(BaseModel):
    """
    types.ChatParticipants
    ID: 0x3cbc93f8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatParticipants', 'ChatParticipants'] = pydantic.Field(
        'types.ChatParticipants',
        alias='_'
    )

    chat_id: int
    participants: list["base.ChatParticipant"]
    version: int
