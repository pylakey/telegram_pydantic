from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerSettings(BaseModel):
    """
    types.messages.PeerSettings
    ID: 0x6880b94d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.PeerSettings', 'PeerSettings'] = pydantic.Field(
        'types.messages.PeerSettings',
        alias='_'
    )

    settings: "base.PeerSettings"
    chats: list["base.Chat"]
    users: list["base.User"]
