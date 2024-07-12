from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadFeaturedStickers(BaseModel):
    """
    functions.messages.ReadFeaturedStickers
    ID: 0x5b118126
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReadFeaturedStickers', 'ReadFeaturedStickers'] = pydantic.Field(
        'functions.messages.ReadFeaturedStickers',
        alias='_'
    )

    id: list[int]
