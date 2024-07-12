from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetTopReactions(BaseModel):
    """
    functions.messages.GetTopReactions
    ID: 0xbb8125ba
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetTopReactions', 'GetTopReactions'] = pydantic.Field(
        'functions.messages.GetTopReactions',
        alias='_'
    )

    limit: int
    hash: int
