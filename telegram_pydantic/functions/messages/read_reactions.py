from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadReactions(BaseModel):
    """
    functions.messages.ReadReactions
    ID: 0x54aa7f8e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReadReactions', 'ReadReactions'] = pydantic.Field(
        'functions.messages.ReadReactions',
        alias='_'
    )

    peer: "base.InputPeer"
    top_msg_id: typing.Optional[int] = None
