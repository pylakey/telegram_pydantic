from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UnpinAllMessages(BaseModel):
    """
    functions.messages.UnpinAllMessages
    ID: 0xee22b9a8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.UnpinAllMessages', 'UnpinAllMessages'] = pydantic.Field(
        'functions.messages.UnpinAllMessages',
        alias='_'
    )

    peer: "base.InputPeer"
    top_msg_id: typing.Optional[int] = None
