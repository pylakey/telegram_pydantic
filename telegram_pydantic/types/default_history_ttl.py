from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DefaultHistoryTTL(BaseModel):
    """
    types.DefaultHistoryTTL
    ID: 0x43b46b20
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DefaultHistoryTTL', 'DefaultHistoryTTL'] = pydantic.Field(
        'types.DefaultHistoryTTL',
        alias='_'
    )

    period: int
