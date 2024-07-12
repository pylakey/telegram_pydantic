from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaPhoto(BaseModel):
    """
    types.MessageMediaPhoto
    ID: 0x695150d7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaPhoto', 'MessageMediaPhoto'] = pydantic.Field(
        'types.MessageMediaPhoto',
        alias='_'
    )

    spoiler: typing.Optional[bool] = None
    photo: typing.Optional["base.Photo"] = None
    ttl_seconds: typing.Optional[int] = None
