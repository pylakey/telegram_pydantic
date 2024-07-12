from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMessageStats(BaseModel):
    """
    functions.stats.GetMessageStats
    ID: 0xb6e0a3f5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetMessageStats', 'GetMessageStats'] = pydantic.Field(
        'functions.stats.GetMessageStats',
        alias='_'
    )

    channel: "base.InputChannel"
    msg_id: int
    dark: typing.Optional[bool] = None
