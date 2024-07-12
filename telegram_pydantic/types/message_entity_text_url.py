from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityTextUrl(BaseModel):
    """
    types.MessageEntityTextUrl
    ID: 0x76a6d327
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityTextUrl', 'MessageEntityTextUrl'] = pydantic.Field(
        'types.MessageEntityTextUrl',
        alias='_'
    )

    offset: int
    length: int
    url: str
