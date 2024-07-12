from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedChatInvite(BaseModel):
    """
    types.messages.ExportedChatInvite
    ID: 0x1871be50
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ExportedChatInvite', 'ExportedChatInvite'] = pydantic.Field(
        'types.messages.ExportedChatInvite',
        alias='_'
    )

    invite: "base.ExportedChatInvite"
    users: list["base.User"]
