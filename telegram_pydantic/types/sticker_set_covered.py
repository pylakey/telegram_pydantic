from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerSetCovered(BaseModel):
    """
    types.StickerSetCovered
    ID: 0x6410a5d2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StickerSetCovered', 'StickerSetCovered'] = pydantic.Field(
        'types.StickerSetCovered',
        alias='_'
    )

    set: "base.StickerSet"
    cover: "base.Document"
