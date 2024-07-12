from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Photo(BaseModel):
    """
    types.photos.Photo
    ID: 0x20212ca8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.photos.Photo', 'Photo'] = pydantic.Field(
        'types.photos.Photo',
        alias='_'
    )

    photo: "base.Photo"
    users: list["base.User"]
