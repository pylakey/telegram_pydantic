from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecentMeUrls(BaseModel):
    """
    types.help.RecentMeUrls
    ID: 0xe0310d7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.RecentMeUrls', 'RecentMeUrls'] = pydantic.Field(
        'types.help.RecentMeUrls',
        alias='_'
    )

    urls: list["base.RecentMeUrl"]
    chats: list["base.Chat"]
    users: list["base.User"]
