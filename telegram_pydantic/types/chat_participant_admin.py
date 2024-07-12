from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatParticipantAdmin(BaseModel):
    """
    types.ChatParticipantAdmin
    ID: 0xa0933f5b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatParticipantAdmin', 'ChatParticipantAdmin'] = pydantic.Field(
        'types.ChatParticipantAdmin',
        alias='_'
    )

    user_id: int
    inviter_id: int
    date: Datetime
