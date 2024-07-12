from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsGraphAsync(BaseModel):
    """
    types.StatsGraphAsync
    ID: 0x4a27eb2d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsGraphAsync', 'StatsGraphAsync'] = pydantic.Field(
        'types.StatsGraphAsync',
        alias='_'
    )

    token: str
