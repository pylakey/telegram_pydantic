from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchResultPosition(BaseModel):
    """
    types.SearchResultPosition
    ID: 0x7f648b67
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SearchResultPosition', 'SearchResultPosition'] = pydantic.Field(
        'types.SearchResultPosition',
        alias='_'
    )

    msg_id: int
    date: Datetime
    offset: int
