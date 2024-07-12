from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReorderStickerSets(BaseModel):
    """
    functions.messages.ReorderStickerSets
    ID: 0x78337739
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReorderStickerSets', 'ReorderStickerSets'] = pydantic.Field(
        'functions.messages.ReorderStickerSets',
        alias='_'
    )

    order: list[int]
    masks: typing.Optional[bool] = None
    emojis: typing.Optional[bool] = None
