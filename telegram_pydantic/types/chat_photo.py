from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatPhoto(BaseModel):
    """
    types.ChatPhoto
    ID: 0x1c6e1c11
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatPhoto', 'ChatPhoto'] = pydantic.Field(
        'types.ChatPhoto',
        alias='_'
    )

    photo_id: int
    dc_id: int
    has_video: typing.Optional[bool] = None
    stripped_thumb: typing.Optional[Bytes] = None
