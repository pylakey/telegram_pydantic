from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ArchivedStickers(BaseModel):
    """
    types.messages.ArchivedStickers
    ID: 0x4fcba9c8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ArchivedStickers', 'ArchivedStickers'] = pydantic.Field(
        'types.messages.ArchivedStickers',
        alias='_'
    )

    count: int
    sets: list["base.StickerSetCovered"]
