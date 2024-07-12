from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatAdminWithInvites(BaseModel):
    """
    types.ChatAdminWithInvites
    ID: 0xf2ecef23
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatAdminWithInvites', 'ChatAdminWithInvites'] = pydantic.Field(
        'types.ChatAdminWithInvites',
        alias='_'
    )

    admin_id: int
    invites_count: int
    revoked_invites_count: int
