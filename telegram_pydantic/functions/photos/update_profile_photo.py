from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateProfilePhoto(BaseModel):
    """
    functions.photos.UpdateProfilePhoto
    ID: 0x9e82039
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.photos.UpdateProfilePhoto', 'UpdateProfilePhoto'] = pydantic.Field(
        'functions.photos.UpdateProfilePhoto',
        alias='_'
    )

    id: "base.InputPhoto"
    fallback: typing.Optional[bool] = None
    bot: typing.Optional["base.InputUser"] = None
