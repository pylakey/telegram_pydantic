from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendQuickReplyMessages(BaseModel):
    """
    functions.messages.SendQuickReplyMessages
    ID: 0x6c750de1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendQuickReplyMessages', 'SendQuickReplyMessages'] = pydantic.Field(
        'functions.messages.SendQuickReplyMessages',
        alias='_'
    )

    peer: "base.InputPeer"
    shortcut_id: int
    id: list[int]
    random_id: list[int]
