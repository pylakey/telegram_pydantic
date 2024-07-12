from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatInvitePeek(BaseModel):
    """
    types.ChatInvitePeek
    ID: 0x61695cb0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatInvitePeek', 'ChatInvitePeek'] = pydantic.Field(
        'types.ChatInvitePeek',
        alias='_'
    )

    chat: "base.Chat"
    expires: Datetime
