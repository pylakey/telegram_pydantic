from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetExportedChatInvites(BaseModel):
    """
    functions.messages.GetExportedChatInvites
    ID: 0xa2b5a3f6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetExportedChatInvites', 'GetExportedChatInvites'] = pydantic.Field(
        'functions.messages.GetExportedChatInvites',
        alias='_'
    )

    peer: "base.InputPeer"
    admin_id: "base.InputUser"
    limit: int
    revoked: typing.Optional[bool] = None
    offset_date: typing.Optional[Datetime] = None
    offset_link: typing.Optional[str] = None
