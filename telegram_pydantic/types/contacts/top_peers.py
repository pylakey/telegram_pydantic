from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeers(BaseModel):
    """
    types.contacts.TopPeers
    ID: 0x70b772a8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.TopPeers', 'TopPeers'] = pydantic.Field(
        'types.contacts.TopPeers',
        alias='_'
    )

    categories: list["base.TopPeerCategoryPeers"]
    chats: list["base.Chat"]
    users: list["base.User"]
