from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecentMeUrlChatInvite(BaseModel):
    """
    types.RecentMeUrlChatInvite
    ID: 0xeb49081d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RecentMeUrlChatInvite', 'RecentMeUrlChatInvite'] = pydantic.Field(
        'types.RecentMeUrlChatInvite',
        alias='_'
    )

    url: str
    chat_invite: "base.ChatInvite"
