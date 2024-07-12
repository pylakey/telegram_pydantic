from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityUnknown(BaseModel):
    """
    types.MessageEntityUnknown
    ID: 0xbb92ba95
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityUnknown', 'MessageEntityUnknown'] = pydantic.Field(
        'types.MessageEntityUnknown',
        alias='_'
    )

    offset: int
    length: int
