from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsAbsValueAndPrev(BaseModel):
    """
    types.StatsAbsValueAndPrev
    ID: 0xcb43acde
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsAbsValueAndPrev', 'StatsAbsValueAndPrev'] = pydantic.Field(
        'types.StatsAbsValueAndPrev',
        alias='_'
    )

    current: float
    previous: float
