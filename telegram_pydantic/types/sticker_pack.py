from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerPack(BaseModel):
    """
    types.StickerPack
    ID: 0x12b299d4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StickerPack', 'StickerPack'] = pydantic.Field(
        'types.StickerPack',
        alias='_'
    )

    emoticon: str
    documents: list[int]
