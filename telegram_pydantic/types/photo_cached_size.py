from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhotoCachedSize(BaseModel):
    """
    types.PhotoCachedSize
    ID: 0x21e1ad6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhotoCachedSize', 'PhotoCachedSize'] = pydantic.Field(
        'types.PhotoCachedSize',
        alias='_'
    )

    type: str
    w: int
    h: int
    bytes: Bytes
