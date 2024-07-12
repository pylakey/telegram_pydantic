from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetAnimatedEmoji(BaseModel):
    """
    types.InputStickerSetAnimatedEmoji
    ID: 0x28703c8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetAnimatedEmoji', 'InputStickerSetAnimatedEmoji'] = pydantic.Field(
        'types.InputStickerSetAnimatedEmoji',
        alias='_'
    )

