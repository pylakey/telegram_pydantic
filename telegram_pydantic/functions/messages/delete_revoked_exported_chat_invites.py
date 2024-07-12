from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteRevokedExportedChatInvites(BaseModel):
    """
    functions.messages.DeleteRevokedExportedChatInvites
    ID: 0x56987bd5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteRevokedExportedChatInvites', 'DeleteRevokedExportedChatInvites'] = pydantic.Field(
        'functions.messages.DeleteRevokedExportedChatInvites',
        alias='_'
    )

    peer: "base.InputPeer"
    admin_id: "base.InputUser"
