from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadFeaturedEmojiStickers(BaseModel):
    """
    types.UpdateReadFeaturedEmojiStickers
    ID: 0xfb4c496c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadFeaturedEmojiStickers', 'UpdateReadFeaturedEmojiStickers'] = pydantic.Field(
        'types.UpdateReadFeaturedEmojiStickers',
        alias='_'
    )

