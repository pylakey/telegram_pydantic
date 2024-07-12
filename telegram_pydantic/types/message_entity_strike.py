from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityStrike(BaseModel):
    """
    types.MessageEntityStrike
    ID: 0xbf0693d4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityStrike', 'MessageEntityStrike'] = pydantic.Field(
        'types.MessageEntityStrike',
        alias='_'
    )

    offset: int
    length: int
