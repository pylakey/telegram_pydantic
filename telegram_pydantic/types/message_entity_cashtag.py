from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityCashtag(BaseModel):
    """
    types.MessageEntityCashtag
    ID: 0x4c4e743f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityCashtag', 'MessageEntityCashtag'] = pydantic.Field(
        'types.MessageEntityCashtag',
        alias='_'
    )

    offset: int
    length: int
