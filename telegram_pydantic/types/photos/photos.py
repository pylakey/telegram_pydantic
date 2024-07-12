from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Photos(BaseModel):
    """
    types.photos.Photos
    ID: 0x8dca6aa5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.photos.Photos', 'Photos'] = pydantic.Field(
        'types.photos.Photos',
        alias='_'
    )

    photos: list["base.Photo"]
    users: list["base.User"]
