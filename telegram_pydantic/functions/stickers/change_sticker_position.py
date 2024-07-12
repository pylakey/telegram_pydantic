from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChangeStickerPosition(BaseModel):
    """
    functions.stickers.ChangeStickerPosition
    ID: 0xffb6d4ca
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stickers.ChangeStickerPosition', 'ChangeStickerPosition'] = pydantic.Field(
        'functions.stickers.ChangeStickerPosition',
        alias='_'
    )

    sticker: "base.InputDocument"
    position: int
