from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessChatLink(BaseModel):
    """
    types.BusinessChatLink
    ID: 0xb4ae666f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessChatLink', 'BusinessChatLink'] = pydantic.Field(
        'types.BusinessChatLink',
        alias='_'
    )

    link: str
    message: str
    views: int
    entities: typing.Optional[list["base.MessageEntity"]] = None
    title: typing.Optional[str] = None
