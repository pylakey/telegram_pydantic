from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MediaAreaChannelPost(BaseModel):
    """
    types.MediaAreaChannelPost
    ID: 0x770416af
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MediaAreaChannelPost', 'MediaAreaChannelPost'] = pydantic.Field(
        'types.MediaAreaChannelPost',
        alias='_'
    )

    coordinates: "base.MediaAreaCoordinates"
    channel_id: int
    msg_id: int
