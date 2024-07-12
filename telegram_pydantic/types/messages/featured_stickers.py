from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FeaturedStickers(BaseModel):
    """
    types.messages.FeaturedStickers
    ID: 0xbe382906
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.FeaturedStickers', 'FeaturedStickers'] = pydantic.Field(
        'types.messages.FeaturedStickers',
        alias='_'
    )

    hash: int
    count: int
    sets: list["base.StickerSetCovered"]
    unread: list[int]
    premium: typing.Optional[bool] = None
