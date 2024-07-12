from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerSetFullCovered(BaseModel):
    """
    types.StickerSetFullCovered
    ID: 0x40d13c0e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StickerSetFullCovered', 'StickerSetFullCovered'] = pydantic.Field(
        'types.StickerSetFullCovered',
        alias='_'
    )

    set: "base.StickerSet"
    packs: list["base.StickerPack"]
    keywords: list["base.StickerKeyword"]
    documents: list["base.Document"]
