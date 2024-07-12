from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelDifference(BaseModel):
    """
    types.updates.ChannelDifference
    ID: 0x2064674e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.updates.ChannelDifference', 'ChannelDifference'] = pydantic.Field(
        'types.updates.ChannelDifference',
        alias='_'
    )

    pts: int
    new_messages: list["base.Message"]
    other_updates: list["base.Update"]
    chats: list["base.Chat"]
    users: list["base.User"]
    final: typing.Optional[bool] = None
    timeout: typing.Optional[int] = None
