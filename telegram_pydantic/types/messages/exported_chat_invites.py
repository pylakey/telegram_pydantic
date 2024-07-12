from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedChatInvites(BaseModel):
    """
    types.messages.ExportedChatInvites
    ID: 0xbdc62dcc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ExportedChatInvites', 'ExportedChatInvites'] = pydantic.Field(
        'types.messages.ExportedChatInvites',
        alias='_'
    )

    count: int
    invites: list["base.ExportedChatInvite"]
    users: list["base.User"]
