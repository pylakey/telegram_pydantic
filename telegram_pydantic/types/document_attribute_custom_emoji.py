from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DocumentAttributeCustomEmoji(BaseModel):
    """
    types.DocumentAttributeCustomEmoji
    ID: 0xfd149899
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DocumentAttributeCustomEmoji', 'DocumentAttributeCustomEmoji'] = pydantic.Field(
        'types.DocumentAttributeCustomEmoji',
        alias='_'
    )

    alt: str
    stickerset: "base.InputStickerSet"
    free: typing.Optional[bool] = None
    text_color: typing.Optional[bool] = None
