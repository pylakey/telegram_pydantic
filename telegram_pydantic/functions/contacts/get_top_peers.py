from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetTopPeers(BaseModel):
    """
    functions.contacts.GetTopPeers
    ID: 0x973478b6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.GetTopPeers', 'GetTopPeers'] = pydantic.Field(
        'functions.contacts.GetTopPeers',
        alias='_'
    )

    offset: int
    limit: int
    hash: int
    correspondents: typing.Optional[bool] = None
    bots_pm: typing.Optional[bool] = None
    bots_inline: typing.Optional[bool] = None
    phone_calls: typing.Optional[bool] = None
    forward_users: typing.Optional[bool] = None
    forward_chats: typing.Optional[bool] = None
    groups: typing.Optional[bool] = None
    channels: typing.Optional[bool] = None
