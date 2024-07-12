from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePeerWallpaper(BaseModel):
    """
    types.UpdatePeerWallpaper
    ID: 0xae3f101d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePeerWallpaper', 'UpdatePeerWallpaper'] = pydantic.Field(
        'types.UpdatePeerWallpaper',
        alias='_'
    )

    peer: "base.Peer"
    wallpaper_overridden: typing.Optional[bool] = None
    wallpaper: typing.Optional["base.WallPaper"] = None
