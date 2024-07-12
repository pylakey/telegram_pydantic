from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaUploadedPhoto(BaseModel):
    """
    types.InputMediaUploadedPhoto
    ID: 0x1e287d04
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaUploadedPhoto', 'InputMediaUploadedPhoto'] = pydantic.Field(
        'types.InputMediaUploadedPhoto',
        alias='_'
    )

    file: "base.InputFile"
    spoiler: typing.Optional[bool] = None
    stickers: typing.Optional[list["base.InputDocument"]] = None
    ttl_seconds: typing.Optional[int] = None
