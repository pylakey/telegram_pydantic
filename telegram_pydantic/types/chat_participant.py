from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatParticipant(BaseModel):
    """
    types.ChatParticipant
    ID: 0xc02d4007
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatParticipant', 'ChatParticipant'] = pydantic.Field(
        'types.ChatParticipant',
        alias='_'
    )

    user_id: int
    inviter_id: int
    date: Datetime
