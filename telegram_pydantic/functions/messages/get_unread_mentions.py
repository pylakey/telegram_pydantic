from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetUnreadMentions(BaseModel):
    """
    functions.messages.GetUnreadMentions
    ID: 0xf107e790
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetUnreadMentions', 'GetUnreadMentions'] = pydantic.Field(
        'functions.messages.GetUnreadMentions',
        alias='_'
    )

    peer: "base.InputPeer"
    offset_id: int
    add_offset: int
    limit: int
    max_id: int
    min_id: int
    top_msg_id: typing.Optional[int] = None
