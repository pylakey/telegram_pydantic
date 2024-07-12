from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessAwayMessageScheduleOutsideWorkHours(BaseModel):
    """
    types.BusinessAwayMessageScheduleOutsideWorkHours
    ID: 0xc3f2f501
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessAwayMessageScheduleOutsideWorkHours', 'BusinessAwayMessageScheduleOutsideWorkHours'] = pydantic.Field(
        'types.BusinessAwayMessageScheduleOutsideWorkHours',
        alias='_'
    )

