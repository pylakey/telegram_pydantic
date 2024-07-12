from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportChatInvite(BaseModel):
    """
    functions.messages.ExportChatInvite
    ID: 0xa02ce5d5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ExportChatInvite', 'ExportChatInvite'] = pydantic.Field(
        'functions.messages.ExportChatInvite',
        alias='_'
    )

    peer: "base.InputPeer"
    legacy_revoke_permanent: typing.Optional[bool] = None
    request_needed: typing.Optional[bool] = None
    expire_date: Datetime
    usage_limit: typing.Optional[int] = None
    title: typing.Optional[str] = None
