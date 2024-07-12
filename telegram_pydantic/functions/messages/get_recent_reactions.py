from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetRecentReactions(BaseModel):
    """
    functions.messages.GetRecentReactions
    ID: 0x39461db2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetRecentReactions', 'GetRecentReactions'] = pydantic.Field(
        'functions.messages.GetRecentReactions',
        alias='_'
    )

    limit: int
    hash: int
