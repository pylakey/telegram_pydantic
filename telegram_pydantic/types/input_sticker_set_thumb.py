from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetThumb(BaseModel):
    """
    types.InputStickerSetThumb
    ID: 0x9d84f3db
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetThumb', 'InputStickerSetThumb'] = pydantic.Field(
        'types.InputStickerSetThumb',
        alias='_'
    )

    stickerset: "base.InputStickerSet"
    thumb_version: int
