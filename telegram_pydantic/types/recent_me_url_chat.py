from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecentMeUrlChat(BaseModel):
    """
    types.RecentMeUrlChat
    ID: 0xb2da71d2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RecentMeUrlChat', 'RecentMeUrlChat'] = pydantic.Field(
        'types.RecentMeUrlChat',
        alias='_'
    )

    url: str
    chat_id: int
