from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DocumentAttributeSticker(BaseModel):
    """
    types.DocumentAttributeSticker
    ID: 0x6319d612
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DocumentAttributeSticker', 'DocumentAttributeSticker'] = pydantic.Field(
        'types.DocumentAttributeSticker',
        alias='_'
    )

    alt: str
    stickerset: "base.InputStickerSet"
    mask: typing.Optional[bool] = None
    mask_coords: typing.Optional["base.MaskCoords"] = None
