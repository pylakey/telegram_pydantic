from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchResultsCalendarPeriod(BaseModel):
    """
    types.SearchResultsCalendarPeriod
    ID: 0xc9b0539f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SearchResultsCalendarPeriod', 'SearchResultsCalendarPeriod'] = pydantic.Field(
        'types.SearchResultsCalendarPeriod',
        alias='_'
    )

    date: Datetime
    min_msg_id: int
    max_msg_id: int
    count: int
