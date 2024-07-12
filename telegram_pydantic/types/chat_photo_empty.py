from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatPhotoEmpty(BaseModel):
    """
    types.ChatPhotoEmpty
    ID: 0x37c1011c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatPhotoEmpty', 'ChatPhotoEmpty'] = pydantic.Field(
        'types.ChatPhotoEmpty',
        alias='_'
    )

