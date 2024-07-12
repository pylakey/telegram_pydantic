from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class OutboxReadDate(BaseModel):
    """
    types.OutboxReadDate
    ID: 0x3bb842ac
    Layer: 181
    """
    QUALNAME: typing.Literal['types.OutboxReadDate', 'OutboxReadDate'] = pydantic.Field(
        'types.OutboxReadDate',
        alias='_'
    )

    date: Datetime
