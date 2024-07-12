from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageRange(BaseModel):
    """
    types.MessageRange
    ID: 0xae30253
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageRange', 'MessageRange'] = pydantic.Field(
        'types.MessageRange',
        alias='_'
    )

    min_id: int
    max_id: int
