from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AffectedHistory(BaseModel):
    """
    types.messages.AffectedHistory
    ID: 0xb45c69d1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.AffectedHistory', 'AffectedHistory'] = pydantic.Field(
        'types.messages.AffectedHistory',
        alias='_'
    )

    pts: int
    pts_count: int
    offset: int
