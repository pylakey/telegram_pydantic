from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AffectedFoundMessages(BaseModel):
    """
    types.messages.AffectedFoundMessages
    ID: 0xef8d3e6c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.AffectedFoundMessages', 'AffectedFoundMessages'] = pydantic.Field(
        'types.messages.AffectedFoundMessages',
        alias='_'
    )

    pts: int
    pts_count: int
    offset: int
    messages: list[int]
