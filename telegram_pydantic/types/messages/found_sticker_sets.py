from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FoundStickerSets(BaseModel):
    """
    types.messages.FoundStickerSets
    ID: 0x8af09dd2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.FoundStickerSets', 'FoundStickerSets'] = pydantic.Field(
        'types.messages.FoundStickerSets',
        alias='_'
    )

    hash: int
    sets: list["base.StickerSetCovered"]
