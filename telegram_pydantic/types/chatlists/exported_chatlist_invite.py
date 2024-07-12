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
    types.chatlists.ExportedChatlistInvite
    ID: 0x10e6e3a6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.chatlists.ExportedChatlistInvite', 'ExportedChatlistInvite'] = pydantic.Field(
        'types.chatlists.ExportedChatlistInvite',
        alias='_'
    )

    filter: "base.DialogFilter"
    invite: "base.ExportedChatlistInvite"
