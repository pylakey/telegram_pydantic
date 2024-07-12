from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaEmpty(BaseModel):
    """
    types.MessageMediaEmpty
    ID: 0x3ded6320
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaEmpty', 'MessageMediaEmpty'] = pydantic.Field(
        'types.MessageMediaEmpty',
        alias='_'
    )

