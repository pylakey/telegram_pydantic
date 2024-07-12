from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessChatLinks(BaseModel):
    """
    types.account.BusinessChatLinks
    ID: 0xec43a2d1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.BusinessChatLinks', 'BusinessChatLinks'] = pydantic.Field(
        'types.account.BusinessChatLinks',
        alias='_'
    )

    links: list["base.BusinessChatLink"]
    chats: list["base.Chat"]
    users: list["base.User"]
