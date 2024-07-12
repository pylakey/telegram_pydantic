from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatParticipantsForbidden(BaseModel):
    """
    types.ChatParticipantsForbidden
    ID: 0x8763d3e1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatParticipantsForbidden', 'ChatParticipantsForbidden'] = pydantic.Field(
        'types.ChatParticipantsForbidden',
        alias='_'
    )

    chat_id: int
    self_participant: typing.Optional["base.ChatParticipant"] = None
