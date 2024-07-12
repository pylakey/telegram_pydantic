from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaDice(BaseModel):
    """
    types.MessageMediaDice
    ID: 0x3f7ee58b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaDice', 'MessageMediaDice'] = pydantic.Field(
        'types.MessageMediaDice',
        alias='_'
    )

    value: int
    emoticon: str
