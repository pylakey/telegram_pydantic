from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RemoveStickerFromSet(BaseModel):
    """
    functions.stickers.RemoveStickerFromSet
    ID: 0xf7760f51
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stickers.RemoveStickerFromSet', 'RemoveStickerFromSet'] = pydantic.Field(
        'functions.stickers.RemoveStickerFromSet',
        alias='_'
    )

    sticker: "base.InputDocument"
