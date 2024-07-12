from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchResultsCalendar(BaseModel):
    """
    types.messages.SearchResultsCalendar
    ID: 0x147ee23c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SearchResultsCalendar', 'SearchResultsCalendar'] = pydantic.Field(
        'types.messages.SearchResultsCalendar',
        alias='_'
    )

    count: int
    min_date: Datetime
    min_msg_id: int
    periods: list["base.SearchResultsCalendarPeriod"]
    messages: list["base.Message"]
    chats: list["base.Chat"]
    users: list["base.User"]
    inexact: typing.Optional[bool] = None
    offset_id_offset: typing.Optional[int] = None
