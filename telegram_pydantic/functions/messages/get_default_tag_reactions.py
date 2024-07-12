from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDefaultTagReactions(BaseModel):
    """
    functions.messages.GetDefaultTagReactions
    ID: 0xbdf93428
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDefaultTagReactions', 'GetDefaultTagReactions'] = pydantic.Field(
        'functions.messages.GetDefaultTagReactions',
        alias='_'
    )

    hash: int
