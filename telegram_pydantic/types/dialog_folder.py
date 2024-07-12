from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DialogFolder(BaseModel):
    """
    types.DialogFolder
    ID: 0x71bd134c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DialogFolder', 'DialogFolder'] = pydantic.Field(
        'types.DialogFolder',
        alias='_'
    )

    folder: "base.Folder"
    peer: "base.Peer"
    top_message: int
    unread_muted_peers_count: int
    unread_unmuted_peers_count: int
    unread_muted_messages_count: int
    unread_unmuted_messages_count: int
    pinned: typing.Optional[bool] = None
