from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateMoveStickerSetToTop(BaseModel):
    """
    types.UpdateMoveStickerSetToTop
    ID: 0x86fccf85
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateMoveStickerSetToTop', 'UpdateMoveStickerSetToTop'] = pydantic.Field(
        'types.UpdateMoveStickerSetToTop',
        alias='_'
    )

    stickerset: int
    masks: typing.Optional[bool] = None
    emojis: typing.Optional[bool] = None
