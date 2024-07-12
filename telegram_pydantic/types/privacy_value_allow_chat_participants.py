from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueAllowChatParticipants(BaseModel):
    """
    types.PrivacyValueAllowChatParticipants
    ID: 0x6b134e8e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueAllowChatParticipants', 'PrivacyValueAllowChatParticipants'] = pydantic.Field(
        'types.PrivacyValueAllowChatParticipants',
        alias='_'
    )

    chats: list[int]
