from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BlockedSlice(BaseModel):
    """
    types.contacts.BlockedSlice
    ID: 0xe1664194
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.BlockedSlice', 'BlockedSlice'] = pydantic.Field(
        'types.contacts.BlockedSlice',
        alias='_'
    )

    count: int
    blocked: list["base.PeerBlocked"]
    chats: list["base.Chat"]
    users: list["base.User"]
