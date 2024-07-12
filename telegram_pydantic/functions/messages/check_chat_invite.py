from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckChatInvite(BaseModel):
    """
    functions.messages.CheckChatInvite
    ID: 0x3eadb1bb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.CheckChatInvite', 'CheckChatInvite'] = pydantic.Field(
        'functions.messages.CheckChatInvite',
        alias='_'
    )

    hash: str
