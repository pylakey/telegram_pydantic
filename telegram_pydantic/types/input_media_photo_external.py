from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaPhotoExternal(BaseModel):
    """
    types.InputMediaPhotoExternal
    ID: 0xe5bbfe1a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaPhotoExternal', 'InputMediaPhotoExternal'] = pydantic.Field(
        'types.InputMediaPhotoExternal',
        alias='_'
    )

    url: str
    spoiler: typing.Optional[bool] = None
    ttl_seconds: typing.Optional[int] = None
