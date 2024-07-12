from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebPage(BaseModel):
    """
    types.messages.WebPage
    ID: 0xfd5e12bd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.WebPage', 'WebPage'] = pydantic.Field(
        'types.messages.WebPage',
        alias='_'
    )

    webpage: "base.WebPage"
    chats: list["base.Chat"]
    users: list["base.User"]
