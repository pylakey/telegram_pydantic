from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetEmojiGenericAnimations(BaseModel):
    """
    types.InputStickerSetEmojiGenericAnimations
    ID: 0x4c4d4ce
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetEmojiGenericAnimations', 'InputStickerSetEmojiGenericAnimations'] = pydantic.Field(
        'types.InputStickerSetEmojiGenericAnimations',
        alias='_'
    )

