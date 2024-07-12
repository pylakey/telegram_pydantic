from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChatParticipantDelete(BaseModel):
    """
    types.UpdateChatParticipantDelete
    ID: 0xe32f3d77
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChatParticipantDelete', 'UpdateChatParticipantDelete'] = pydantic.Field(
        'types.UpdateChatParticipantDelete',
        alias='_'
    )

    chat_id: int
    user_id: int
    version: int
