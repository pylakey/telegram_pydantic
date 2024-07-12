from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsPercentValue(BaseModel):
    """
    types.StatsPercentValue
    ID: 0xcbce2fe0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsPercentValue', 'StatsPercentValue'] = pydantic.Field(
        'types.StatsPercentValue',
        alias='_'
    )

    part: float
    total: float
