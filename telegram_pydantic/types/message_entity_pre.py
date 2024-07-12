from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityPre(BaseModel):
    """
    types.MessageEntityPre
    ID: 0x73924be0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityPre', 'MessageEntityPre'] = pydantic.Field(
        'types.MessageEntityPre',
        alias='_'
    )

    offset: int
    length: int
    language: str
