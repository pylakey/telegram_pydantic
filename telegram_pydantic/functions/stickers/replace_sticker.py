from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReplaceSticker(BaseModel):
    """
    functions.stickers.ReplaceSticker
    ID: 0x4696459a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stickers.ReplaceSticker', 'ReplaceSticker'] = pydantic.Field(
        'functions.stickers.ReplaceSticker',
        alias='_'
    )

    sticker: "base.InputDocument"
    new_sticker: "base.InputStickerSetItem"
