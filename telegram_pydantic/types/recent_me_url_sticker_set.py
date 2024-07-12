from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecentMeUrlStickerSet(BaseModel):
    """
    types.RecentMeUrlStickerSet
    ID: 0xbc0a57dc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RecentMeUrlStickerSet', 'RecentMeUrlStickerSet'] = pydantic.Field(
        'types.RecentMeUrlStickerSet',
        alias='_'
    )

    url: str
    set: "base.StickerSetCovered"
