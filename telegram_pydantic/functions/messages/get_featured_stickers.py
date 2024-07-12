from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetFeaturedStickers(BaseModel):
    """
    functions.messages.GetFeaturedStickers
    ID: 0x64780b14
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetFeaturedStickers', 'GetFeaturedStickers'] = pydantic.Field(
        'functions.messages.GetFeaturedStickers',
        alias='_'
    )

    hash: int
