from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AllStickers(BaseModel):
    """
    types.messages.AllStickers
    ID: 0xcdbbcebb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.AllStickers', 'AllStickers'] = pydantic.Field(
        'types.messages.AllStickers',
        alias='_'
    )

    hash: int
    sets: list["base.StickerSet"]
