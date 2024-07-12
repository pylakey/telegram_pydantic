from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDifference(BaseModel):
    """
    functions.updates.GetDifference
    ID: 0x19c2f763
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.updates.GetDifference', 'GetDifference'] = pydantic.Field(
        'functions.updates.GetDifference',
        alias='_'
    )

    pts: int
    date: Datetime
    qts: int
    pts_limit: typing.Optional[int] = None
    pts_total_limit: typing.Optional[int] = None
    qts_limit: typing.Optional[int] = None
