from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class State(BaseModel):
    """
    types.updates.State
    ID: 0xa56c2a3e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.updates.State', 'State'] = pydantic.Field(
        'types.updates.State',
        alias='_'
    )

    pts: int
    qts: int
    date: Datetime
    seq: int
    unread_count: int
