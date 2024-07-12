from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedInvites(BaseModel):
    """
    types.chatlists.ExportedInvites
    ID: 0x10ab6dc7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.chatlists.ExportedInvites', 'ExportedInvites'] = pydantic.Field(
        'types.chatlists.ExportedInvites',
        alias='_'
    )

    invites: list["base.ExportedChatlistInvite"]
    chats: list["base.Chat"]
    users: list["base.User"]
