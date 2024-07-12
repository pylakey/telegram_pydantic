from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityBold(BaseModel):
    """
    types.MessageEntityBold
    ID: 0xbd610bc9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityBold', 'MessageEntityBold'] = pydantic.Field(
        'types.MessageEntityBold',
        alias='_'
    )

    offset: int
    length: int
