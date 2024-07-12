from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetPremiumGifts(BaseModel):
    """
    types.InputStickerSetPremiumGifts
    ID: 0xc88b3b02
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetPremiumGifts', 'InputStickerSetPremiumGifts'] = pydantic.Field(
        'types.InputStickerSetPremiumGifts',
        alias='_'
    )

