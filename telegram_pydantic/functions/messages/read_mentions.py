from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadMentions(BaseModel):
    """
    functions.messages.ReadMentions
    ID: 0x36e5bf4d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReadMentions', 'ReadMentions'] = pydantic.Field(
        'functions.messages.ReadMentions',
        alias='_'
    )

    peer: "base.InputPeer"
    top_msg_id: typing.Optional[int] = None
