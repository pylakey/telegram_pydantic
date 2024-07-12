from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UploadContactProfilePhoto(BaseModel):
    """
    functions.photos.UploadContactProfilePhoto
    ID: 0xe14c4a71
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.photos.UploadContactProfilePhoto', 'UploadContactProfilePhoto'] = pydantic.Field(
        'functions.photos.UploadContactProfilePhoto',
        alias='_'
    )

    user_id: "base.InputUser"
    suggest: typing.Optional[bool] = None
    save: typing.Optional[bool] = None
    file: typing.Optional["base.InputFile"] = None
    video: typing.Optional["base.InputFile"] = None
    video_start_ts: typing.Optional[float] = None
    video_emoji_markup: typing.Optional["base.VideoSize"] = None
