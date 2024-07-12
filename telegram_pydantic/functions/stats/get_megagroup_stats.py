from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMegagroupStats(BaseModel):
    """
    functions.stats.GetMegagroupStats
    ID: 0xdcdf8607
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetMegagroupStats', 'GetMegagroupStats'] = pydantic.Field(
        'functions.stats.GetMegagroupStats',
        alias='_'
    )

    channel: "base.InputChannel"
    dark: typing.Optional[bool] = None
