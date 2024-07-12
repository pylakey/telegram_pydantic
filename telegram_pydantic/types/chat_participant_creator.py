from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatParticipantCreator(BaseModel):
    """
    types.ChatParticipantCreator
    ID: 0xe46bcee4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatParticipantCreator', 'ChatParticipantCreator'] = pydantic.Field(
        'types.ChatParticipantCreator',
        alias='_'
    )

    user_id: int
