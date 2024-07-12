from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebPageAttributeStickerSet(BaseModel):
    """
    types.WebPageAttributeStickerSet
    ID: 0x50cc03d3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebPageAttributeStickerSet', 'WebPageAttributeStickerSet'] = pydantic.Field(
        'types.WebPageAttributeStickerSet',
        alias='_'
    )

    stickers: list["base.Document"]
    emojis: typing.Optional[bool] = None
    text_color: typing.Optional[bool] = None
