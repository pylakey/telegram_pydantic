from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetEmojiProfilePhotoGroups(BaseModel):
    """
    functions.messages.GetEmojiProfilePhotoGroups
    ID: 0x21a548f3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetEmojiProfilePhotoGroups', 'GetEmojiProfilePhotoGroups'] = pydantic.Field(
        'functions.messages.GetEmojiProfilePhotoGroups',
        alias='_'
    )

    hash: int
