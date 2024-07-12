from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetDefaultHistoryTTL(BaseModel):
    """
    functions.messages.SetDefaultHistoryTTL
    ID: 0x9eb51445
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetDefaultHistoryTTL', 'SetDefaultHistoryTTL'] = pydantic.Field(
        'functions.messages.SetDefaultHistoryTTL',
        alias='_'
    )

    period: int
