from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportChatlistInvite(BaseModel):
    """
    functions.chatlists.ExportChatlistInvite
    ID: 0x8472478e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.ExportChatlistInvite', 'ExportChatlistInvite'] = pydantic.Field(
        'functions.chatlists.ExportChatlistInvite',
        alias='_'
    )

    chatlist: "base.InputChatlist"
    title: str
    peers: list["base.InputPeer"]
