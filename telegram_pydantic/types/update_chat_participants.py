from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChatParticipants(BaseModel):
    """
    types.UpdateChatParticipants
    ID: 0x7761198
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChatParticipants', 'UpdateChatParticipants'] = pydantic.Field(
        'types.UpdateChatParticipants',
        alias='_'
    )

    participants: "base.ChatParticipants"
