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
    types.Photo
    ID: 0xfb197a65
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Photo', 'Photo'] = pydantic.Field(
        'types.Photo',
        alias='_'
    )

    id: int
    access_hash: int
    file_reference: Bytes
    date: Datetime
    sizes: list["base.PhotoSize"]
    dc_id: int
    has_stickers: typing.Optional[bool] = None
    video_sizes: typing.Optional[list["base.VideoSize"]] = None
