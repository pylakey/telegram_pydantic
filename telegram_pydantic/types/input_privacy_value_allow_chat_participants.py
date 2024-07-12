from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueAllowChatParticipants(BaseModel):
    """
    types.InputPrivacyValueAllowChatParticipants
    ID: 0x840649cf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueAllowChatParticipants', 'InputPrivacyValueAllowChatParticipants'] = pydantic.Field(
        'types.InputPrivacyValueAllowChatParticipants',
        alias='_'
    )

    chats: list[int]
