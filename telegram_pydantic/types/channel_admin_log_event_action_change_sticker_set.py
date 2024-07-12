from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeStickerSet(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeStickerSet
    ID: 0xb1c3caa7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeStickerSet', 'ChannelAdminLogEventActionChangeStickerSet'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeStickerSet',
        alias='_'
    )

    prev_stickerset: "base.InputStickerSet"
    new_stickerset: "base.InputStickerSet"
