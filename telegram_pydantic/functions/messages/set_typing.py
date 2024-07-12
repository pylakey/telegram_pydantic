from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetTyping(BaseModel):
    """
    functions.messages.SetTyping
    ID: 0x58943ee2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetTyping', 'SetTyping'] = pydantic.Field(
        'functions.messages.SetTyping',
        alias='_'
    )

    peer: "base.InputPeer"
    action: "base.SendMessageAction"
    top_msg_id: typing.Optional[int] = None
