from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterPhotoVideo(BaseModel):
    """
    types.InputMessagesFilterPhotoVideo
    ID: 0x56e9f0e4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterPhotoVideo', 'InputMessagesFilterPhotoVideo'] = pydantic.Field(
        'types.InputMessagesFilterPhotoVideo',
        alias='_'
    )

