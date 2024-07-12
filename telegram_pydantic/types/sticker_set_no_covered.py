from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerSetNoCovered(BaseModel):
    """
    types.StickerSetNoCovered
    ID: 0x77b15d1c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StickerSetNoCovered', 'StickerSetNoCovered'] = pydantic.Field(
        'types.StickerSetNoCovered',
        alias='_'
    )

    set: "base.StickerSet"
