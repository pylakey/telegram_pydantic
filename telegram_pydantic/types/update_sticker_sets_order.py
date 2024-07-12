from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateStickerSetsOrder(BaseModel):
    """
    types.UpdateStickerSetsOrder
    ID: 0xbb2d201
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateStickerSetsOrder', 'UpdateStickerSetsOrder'] = pydantic.Field(
        'types.UpdateStickerSetsOrder',
        alias='_'
    )

    order: list[int]
    masks: typing.Optional[bool] = None
    emojis: typing.Optional[bool] = None
