from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckShortName(BaseModel):
    """
    functions.stickers.CheckShortName
    ID: 0x284b3639
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stickers.CheckShortName', 'CheckShortName'] = pydantic.Field(
        'functions.stickers.CheckShortName',
        alias='_'
    )

    short_name: str
