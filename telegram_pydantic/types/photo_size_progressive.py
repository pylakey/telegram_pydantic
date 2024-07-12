from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhotoSizeProgressive(BaseModel):
    """
    types.PhotoSizeProgressive
    ID: 0xfa3efb95
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhotoSizeProgressive', 'PhotoSizeProgressive'] = pydantic.Field(
        'types.PhotoSizeProgressive',
        alias='_'
    )

    type: str
    w: int
    h: int
    sizes: list[int]
