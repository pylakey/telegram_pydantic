from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBotCallbackAnswer(BaseModel):
    """
    functions.messages.SetBotCallbackAnswer
    ID: 0xd58f130a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetBotCallbackAnswer', 'SetBotCallbackAnswer'] = pydantic.Field(
        'functions.messages.SetBotCallbackAnswer',
        alias='_'
    )

    query_id: int
    cache_time: int
    alert: typing.Optional[bool] = None
    message: typing.Optional[str] = None
    url: typing.Optional[str] = None
