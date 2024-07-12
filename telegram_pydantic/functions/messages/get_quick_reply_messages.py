from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetQuickReplyMessages(BaseModel):
    """
    functions.messages.GetQuickReplyMessages
    ID: 0x94a495c3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetQuickReplyMessages', 'GetQuickReplyMessages'] = pydantic.Field(
        'functions.messages.GetQuickReplyMessages',
        alias='_'
    )

    shortcut_id: int
    hash: int
    id: typing.Optional[list[int]] = None
