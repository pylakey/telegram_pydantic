from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChatDefaultBannedRights(BaseModel):
    """
    types.UpdateChatDefaultBannedRights
    ID: 0x54c01850
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChatDefaultBannedRights', 'UpdateChatDefaultBannedRights'] = pydantic.Field(
        'types.UpdateChatDefaultBannedRights',
        alias='_'
    )

    peer: "base.Peer"
    default_banned_rights: "base.ChatBannedRights"
    version: int
