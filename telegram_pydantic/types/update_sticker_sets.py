from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateStickerSets(BaseModel):
    """
    types.UpdateStickerSets
    ID: 0x31c24808
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateStickerSets', 'UpdateStickerSets'] = pydantic.Field(
        'types.UpdateStickerSets',
        alias='_'
    )

    masks: typing.Optional[bool] = None
    emojis: typing.Optional[bool] = None
