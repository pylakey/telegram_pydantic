from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SponsoredMessages(BaseModel):
    """
    types.messages.SponsoredMessages
    ID: 0xc9ee1d87
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SponsoredMessages', 'SponsoredMessages'] = pydantic.Field(
        'types.messages.SponsoredMessages',
        alias='_'
    )

    messages: list["base.SponsoredMessage"]
    chats: list["base.Chat"]
    users: list["base.User"]
    posts_between: typing.Optional[int] = None
