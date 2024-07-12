from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPhotoFileLocation(BaseModel):
    """
    types.InputPhotoFileLocation
    ID: 0x40181ffe
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPhotoFileLocation', 'InputPhotoFileLocation'] = pydantic.Field(
        'types.InputPhotoFileLocation',
        alias='_'
    )

    id: int
    access_hash: int
    file_reference: Bytes
    thumb_size: str
