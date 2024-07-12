from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNewStickerSet(BaseModel):
    """
    types.UpdateNewStickerSet
    ID: 0x688a30aa
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateNewStickerSet', 'UpdateNewStickerSet'] = pydantic.Field(
        'types.UpdateNewStickerSet',
        alias='_'
    )

    stickerset: "base.messages.StickerSet"
