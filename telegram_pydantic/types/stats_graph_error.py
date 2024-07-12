from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsGraphError(BaseModel):
    """
    types.StatsGraphError
    ID: 0xbedc9822
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsGraphError', 'StatsGraphError'] = pydantic.Field(
        'types.StatsGraphError',
        alias='_'
    )

    error: str
