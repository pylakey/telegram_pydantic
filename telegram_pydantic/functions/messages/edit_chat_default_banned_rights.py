from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditChatDefaultBannedRights(BaseModel):
    """
    functions.messages.EditChatDefaultBannedRights
    ID: 0xa5866b41
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.EditChatDefaultBannedRights', 'EditChatDefaultBannedRights'] = pydantic.Field(
        'functions.messages.EditChatDefaultBannedRights',
        alias='_'
    )

    peer: "base.InputPeer"
    banned_rights: "base.ChatBannedRights"
