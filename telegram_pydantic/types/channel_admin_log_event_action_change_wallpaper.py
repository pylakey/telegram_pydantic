from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeWallpaper(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeWallpaper
    ID: 0x31bb5d52
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeWallpaper', 'ChannelAdminLogEventActionChangeWallpaper'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeWallpaper',
        alias='_'
    )

    prev_value: "base.WallPaper"
    new_value: "base.WallPaper"
