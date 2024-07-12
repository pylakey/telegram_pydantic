from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditBanned(BaseModel):
    """
    functions.channels.EditBanned
    ID: 0x96e6cd81
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.EditBanned', 'EditBanned'] = pydantic.Field(
        'functions.channels.EditBanned',
        alias='_'
    )

    channel: "base.InputChannel"
    participant: "base.InputPeer"
    banned_rights: "base.ChatBannedRights"
