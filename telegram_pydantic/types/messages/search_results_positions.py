from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchResultsPositions(BaseModel):
    """
    types.messages.SearchResultsPositions
    ID: 0x53b22baf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SearchResultsPositions', 'SearchResultsPositions'] = pydantic.Field(
        'types.messages.SearchResultsPositions',
        alias='_'
    )

    count: int
    positions: list["base.SearchResultsPosition"]
