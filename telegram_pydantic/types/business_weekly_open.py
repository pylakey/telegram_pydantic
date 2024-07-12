from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessWeeklyOpen(BaseModel):
    """
    types.BusinessWeeklyOpen
    ID: 0x120b1ab9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessWeeklyOpen', 'BusinessWeeklyOpen'] = pydantic.Field(
        'types.BusinessWeeklyOpen',
        alias='_'
    )

    start_minute: int
    end_minute: int
