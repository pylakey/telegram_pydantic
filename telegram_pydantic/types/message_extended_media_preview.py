from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageExtendedMediaPreview(BaseModel):
    """
    types.MessageExtendedMediaPreview
    ID: 0xad628cc8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageExtendedMediaPreview', 'MessageExtendedMediaPreview'] = pydantic.Field(
        'types.MessageExtendedMediaPreview',
        alias='_'
    )

    w: typing.Optional[int] = None
    h: typing.Optional[int] = None
    thumb: typing.Optional["base.PhotoSize"] = None
    video_duration: typing.Optional[int] = None
