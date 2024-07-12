from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedChatlistInvite(BaseModel):
    """
    types.ExportedChatlistInvite
    ID: 0xc5181ac
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ExportedChatlistInvite', 'ExportedChatlistInvite'] = pydantic.Field(
        'types.ExportedChatlistInvite',
        alias='_'
    )

    title: str
    url: str
    peers: list["base.Peer"]
