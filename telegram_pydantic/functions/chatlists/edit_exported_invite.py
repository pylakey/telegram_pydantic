from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditExportedInvite(BaseModel):
    """
    functions.chatlists.EditExportedInvite
    ID: 0x653db63d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.EditExportedInvite', 'EditExportedInvite'] = pydantic.Field(
        'functions.chatlists.EditExportedInvite',
        alias='_'
    )

    chatlist: "base.InputChatlist"
    slug: str
    title: typing.Optional[str] = None
    peers: typing.Optional[list["base.InputPeer"]] = None
