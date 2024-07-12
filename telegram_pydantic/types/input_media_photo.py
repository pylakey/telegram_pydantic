from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaPhoto(BaseModel):
    """
    types.InputMediaPhoto
    ID: 0xb3ba0635
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaPhoto', 'InputMediaPhoto'] = pydantic.Field(
        'types.InputMediaPhoto',
        alias='_'
    )

    id: "base.InputPhoto"
    spoiler: typing.Optional[bool] = None
    ttl_seconds: typing.Optional[int] = None
