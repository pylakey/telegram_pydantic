from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetUserPhotos(BaseModel):
    """
    functions.photos.GetUserPhotos
    ID: 0x91cd32a8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.photos.GetUserPhotos', 'GetUserPhotos'] = pydantic.Field(
        'functions.photos.GetUserPhotos',
        alias='_'
    )

    user_id: "base.InputUser"
    offset: int
    max_id: int
    limit: int
