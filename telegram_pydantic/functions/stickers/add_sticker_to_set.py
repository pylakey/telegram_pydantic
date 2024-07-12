from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AddStickerToSet(BaseModel):
    """
    functions.stickers.AddStickerToSet
    ID: 0x8653febe
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stickers.AddStickerToSet', 'AddStickerToSet'] = pydantic.Field(
        'functions.stickers.AddStickerToSet',
        alias='_'
    )

    stickerset: "base.InputStickerSet"
    sticker: "base.InputStickerSetItem"
