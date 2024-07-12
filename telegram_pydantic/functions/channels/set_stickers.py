from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetStickers(BaseModel):
    """
    functions.channels.SetStickers
    ID: 0xea8ca4f9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.SetStickers', 'SetStickers'] = pydantic.Field(
        'functions.channels.SetStickers',
        alias='_'
    )

    channel: "base.InputChannel"
    stickerset: "base.InputStickerSet"
