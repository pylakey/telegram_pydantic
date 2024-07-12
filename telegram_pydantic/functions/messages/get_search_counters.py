from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSearchCounters(BaseModel):
    """
    functions.messages.GetSearchCounters
    ID: 0x1bbcf300
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetSearchCounters', 'GetSearchCounters'] = pydantic.Field(
        'functions.messages.GetSearchCounters',
        alias='_'
    )

    peer: "base.InputPeer"
    filters: list["base.MessagesFilter"]
    saved_peer_id: typing.Optional["base.InputPeer"] = None
    top_msg_id: typing.Optional[int] = None
