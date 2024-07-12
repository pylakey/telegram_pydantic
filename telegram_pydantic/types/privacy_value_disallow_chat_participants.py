from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueDisallowChatParticipants(BaseModel):
    """
    types.PrivacyValueDisallowChatParticipants
    ID: 0x41c87565
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueDisallowChatParticipants', 'PrivacyValueDisallowChatParticipants'] = pydantic.Field(
        'types.PrivacyValueDisallowChatParticipants',
        alias='_'
    )

    chats: list[int]
