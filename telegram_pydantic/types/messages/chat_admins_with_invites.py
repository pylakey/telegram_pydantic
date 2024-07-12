from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatAdminsWithInvites(BaseModel):
    """
    types.messages.ChatAdminsWithInvites
    ID: 0xb69b72d7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ChatAdminsWithInvites', 'ChatAdminsWithInvites'] = pydantic.Field(
        'types.messages.ChatAdminsWithInvites',
        alias='_'
    )

    admins: list["base.ChatAdminWithInvites"]
    users: list["base.User"]
