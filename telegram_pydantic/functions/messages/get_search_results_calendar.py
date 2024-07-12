from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSearchResultsCalendar(BaseModel):
    """
    functions.messages.GetSearchResultsCalendar
    ID: 0x6aa3f6bd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetSearchResultsCalendar', 'GetSearchResultsCalendar'] = pydantic.Field(
        'functions.messages.GetSearchResultsCalendar',
        alias='_'
    )

    peer: "base.InputPeer"
    filter: "base.MessagesFilter"
    offset_id: int
    offset_date: Datetime
    saved_peer_id: typing.Optional["base.InputPeer"] = None
