from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteExportedInvite(BaseModel):
    """
    functions.chatlists.DeleteExportedInvite
    ID: 0x719c5c5e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.DeleteExportedInvite', 'DeleteExportedInvite'] = pydantic.Field(
        'functions.chatlists.DeleteExportedInvite',
        alias='_'
    )

    chatlist: "base.InputChatlist"
    slug: str
