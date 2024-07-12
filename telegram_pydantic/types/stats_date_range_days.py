from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsDateRangeDays(BaseModel):
    """
    types.StatsDateRangeDays
    ID: 0xb637edaf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsDateRangeDays', 'StatsDateRangeDays'] = pydantic.Field(
        'types.StatsDateRangeDays',
        alias='_'
    )

    min_date: Datetime
    max_date: Datetime
