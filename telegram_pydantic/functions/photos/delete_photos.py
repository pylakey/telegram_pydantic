from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeletePhotos(BaseModel):
    """
    functions.photos.DeletePhotos
    ID: 0x87cf7f2f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.photos.DeletePhotos', 'DeletePhotos'] = pydantic.Field(
        'functions.photos.DeletePhotos',
        alias='_'
    )

    id: list["base.InputPhoto"]
