from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetItem(BaseModel):
    """
    types.InputStickerSetItem
    ID: 0x32da9e9c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetItem', 'InputStickerSetItem'] = pydantic.Field(
        'types.InputStickerSetItem',
        alias='_'
    )

    document: "base.InputDocument"
    emoji: str
    mask_coords: typing.Optional["base.MaskCoords"] = None
    keywords: typing.Optional[str] = None
