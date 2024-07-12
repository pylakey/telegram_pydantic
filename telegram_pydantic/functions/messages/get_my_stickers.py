from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMyStickers(BaseModel):
    """
    functions.messages.GetMyStickers
    ID: 0xd0b5e1fc
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetMyStickers', 'GetMyStickers'] = pydantic.Field(
        'functions.messages.GetMyStickers',
        alias='_'
    )

    offset_id: int
    limit: int
