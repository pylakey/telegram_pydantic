from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Search(BaseModel):
    """
    functions.messages.Search
    ID: 0x29ee847a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.Search', 'Search'] = pydantic.Field(
        'functions.messages.Search',
        alias='_'
    )

    peer: "base.InputPeer"
    q: str
    filter: "base.MessagesFilter"
    min_date: Datetime
    max_date: Datetime
    offset_id: int
    add_offset: int
    limit: int
    max_id: int
    min_id: int
    hash: int
    from_id: typing.Optional["base.InputPeer"] = None
    saved_peer_id: typing.Optional["base.InputPeer"] = None
    saved_reaction: typing.Optional[list["base.Reaction"]] = None
    top_msg_id: typing.Optional[int] = None
