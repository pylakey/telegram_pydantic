from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityHashtag(BaseModel):
    """
    types.MessageEntityHashtag
    ID: 0x6f635b0d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityHashtag', 'MessageEntityHashtag'] = pydantic.Field(
        'types.MessageEntityHashtag',
        alias='_'
    )

    offset: int
    length: int
