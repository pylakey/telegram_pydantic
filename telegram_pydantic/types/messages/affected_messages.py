from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AffectedMessages(BaseModel):
    """
    types.messages.AffectedMessages
    ID: 0x84d19185
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.AffectedMessages', 'AffectedMessages'] = pydantic.Field(
        'types.messages.AffectedMessages',
        alias='_'
    )

    pts: int
    pts_count: int
