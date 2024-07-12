from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChangeSticker(BaseModel):
    """
    functions.stickers.ChangeSticker
    ID: 0xf5537ebc
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stickers.ChangeSticker', 'ChangeSticker'] = pydantic.Field(
        'functions.stickers.ChangeSticker',
        alias='_'
    )

    sticker: "base.InputDocument"
    emoji: typing.Optional[str] = None
    mask_coords: typing.Optional["base.MaskCoords"] = None
    keywords: typing.Optional[str] = None
