from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatInviteImporters(BaseModel):
    """
    types.messages.ChatInviteImporters
    ID: 0x81b6b00a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ChatInviteImporters', 'ChatInviteImporters'] = pydantic.Field(
        'types.messages.ChatInviteImporters',
        alias='_'
    )

    count: int
    importers: list["base.ChatInviteImporter"]
    users: list["base.User"]
