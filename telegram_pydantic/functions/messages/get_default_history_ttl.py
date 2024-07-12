from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDefaultHistoryTTL(BaseModel):
    """
    functions.messages.GetDefaultHistoryTTL
    ID: 0x658b7188
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDefaultHistoryTTL', 'GetDefaultHistoryTTL'] = pydantic.Field(
        'functions.messages.GetDefaultHistoryTTL',
        alias='_'
    )

