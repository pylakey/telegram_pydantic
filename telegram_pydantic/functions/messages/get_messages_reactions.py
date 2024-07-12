from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMessagesReactions(BaseModel):
    """
    functions.messages.GetMessagesReactions
    ID: 0x8bba90e6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetMessagesReactions', 'GetMessagesReactions'] = pydantic.Field(
        'functions.messages.GetMessagesReactions',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
