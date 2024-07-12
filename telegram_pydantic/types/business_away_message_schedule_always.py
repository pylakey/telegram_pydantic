from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessAwayMessageScheduleAlways(BaseModel):
    """
    types.BusinessAwayMessageScheduleAlways
    ID: 0xc9b9e2b9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessAwayMessageScheduleAlways', 'BusinessAwayMessageScheduleAlways'] = pydantic.Field(
        'types.BusinessAwayMessageScheduleAlways',
        alias='_'
    )

