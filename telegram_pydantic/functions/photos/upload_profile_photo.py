from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UploadProfilePhoto(BaseModel):
    """
    functions.photos.UploadProfilePhoto
    ID: 0x388a3b5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.photos.UploadProfilePhoto', 'UploadProfilePhoto'] = pydantic.Field(
        'functions.photos.UploadProfilePhoto',
        alias='_'
    )

    fallback: typing.Optional[bool] = None
    bot: typing.Optional["base.InputUser"] = None
    file: typing.Optional["base.InputFile"] = None
    video: typing.Optional["base.InputFile"] = None
    video_start_ts: typing.Optional[float] = None
    video_emoji_markup: typing.Optional["base.VideoSize"] = None
