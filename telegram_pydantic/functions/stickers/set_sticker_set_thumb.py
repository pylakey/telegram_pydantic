from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetStickerSetThumb(BaseModel):
    """
    functions.stickers.SetStickerSetThumb
    ID: 0xa76a5392
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stickers.SetStickerSetThumb', 'SetStickerSetThumb'] = pydantic.Field(
        'functions.stickers.SetStickerSetThumb',
        alias='_'
    )

    stickerset: "base.InputStickerSet"
    thumb: typing.Optional["base.InputDocument"] = None
    thumb_document_id: typing.Optional[int] = None
