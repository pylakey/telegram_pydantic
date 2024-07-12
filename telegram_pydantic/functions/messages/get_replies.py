from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetReplies(BaseModel):
    """
    functions.messages.GetReplies
    ID: 0x22ddd30c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetReplies', 'GetReplies'] = pydantic.Field(
        'functions.messages.GetReplies',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    offset_id: int
    offset_date: Datetime
    add_offset: int
    limit: int
    max_id: int
    min_id: int
    hash: int
