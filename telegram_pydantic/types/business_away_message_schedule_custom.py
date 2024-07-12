from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessAwayMessageScheduleCustom(BaseModel):
    """
    types.BusinessAwayMessageScheduleCustom
    ID: 0xcc4d9ecc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessAwayMessageScheduleCustom', 'BusinessAwayMessageScheduleCustom'] = pydantic.Field(
        'types.BusinessAwayMessageScheduleCustom',
        alias='_'
    )

    start_date: Datetime
    end_date: Datetime
