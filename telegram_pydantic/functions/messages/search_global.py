from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchGlobal(BaseModel):
    """
    functions.messages.SearchGlobal
    ID: 0x4bc6589a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SearchGlobal', 'SearchGlobal'] = pydantic.Field(
        'functions.messages.SearchGlobal',
        alias='_'
    )

    q: str
    filter: "base.MessagesFilter"
    min_date: Datetime
    max_date: Datetime
    offset_rate: int
    offset_peer: "base.InputPeer"
    offset_id: int
    limit: int
    broadcasts_only: typing.Optional[bool] = None
    folder_id: typing.Optional[int] = None
