from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerSet(BaseModel):
    """
    types.messages.StickerSet
    ID: 0x6e153f16
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.StickerSet', 'StickerSet'] = pydantic.Field(
        'types.messages.StickerSet',
        alias='_'
    )

    set: "base.StickerSet"
    packs: list["base.StickerPack"]
    keywords: list["base.StickerKeyword"]
    documents: list["base.Document"]
