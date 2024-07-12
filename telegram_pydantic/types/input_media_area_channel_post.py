from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaAreaChannelPost(BaseModel):
    """
    types.InputMediaAreaChannelPost
    ID: 0x2271f2bf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaAreaChannelPost', 'InputMediaAreaChannelPost'] = pydantic.Field(
        'types.InputMediaAreaChannelPost',
        alias='_'
    )

    coordinates: "base.MediaAreaCoordinates"
    channel: "base.InputChannel"
    msg_id: int
