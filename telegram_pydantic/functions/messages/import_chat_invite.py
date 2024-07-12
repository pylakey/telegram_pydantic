from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ImportChatInvite(BaseModel):
    """
    functions.messages.ImportChatInvite
    ID: 0x6c50051c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ImportChatInvite', 'ImportChatInvite'] = pydantic.Field(
        'functions.messages.ImportChatInvite',
        alias='_'
    )

    hash: str
