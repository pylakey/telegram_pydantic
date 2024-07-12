from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhotoSize(BaseModel):
    """
    types.PhotoSize
    ID: 0x75c78e60
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhotoSize', 'PhotoSize'] = pydantic.Field(
        'types.PhotoSize',
        alias='_'
    )

    type: str
    w: int
    h: int
    size: int
