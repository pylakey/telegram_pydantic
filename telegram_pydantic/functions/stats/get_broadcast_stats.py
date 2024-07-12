from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBroadcastStats(BaseModel):
    """
    functions.stats.GetBroadcastStats
    ID: 0xab42441a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetBroadcastStats', 'GetBroadcastStats'] = pydantic.Field(
        'functions.stats.GetBroadcastStats',
        alias='_'
    )

    channel: "base.InputChannel"
    dark: typing.Optional[bool] = None
