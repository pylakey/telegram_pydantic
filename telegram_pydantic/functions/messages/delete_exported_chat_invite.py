from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteExportedChatInvite(BaseModel):
    """
    functions.messages.DeleteExportedChatInvite
    ID: 0xd464a42b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteExportedChatInvite', 'DeleteExportedChatInvite'] = pydantic.Field(
        'functions.messages.DeleteExportedChatInvite',
        alias='_'
    )

    peer: "base.InputPeer"
    link: str
