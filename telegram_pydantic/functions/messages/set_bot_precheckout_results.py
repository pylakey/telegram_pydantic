from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBotPrecheckoutResults(BaseModel):
    """
    functions.messages.SetBotPrecheckoutResults
    ID: 0x9c2dd95
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetBotPrecheckoutResults', 'SetBotPrecheckoutResults'] = pydantic.Field(
        'functions.messages.SetBotPrecheckoutResults',
        alias='_'
    )

    query_id: int
    success: typing.Optional[bool] = None
    error: typing.Optional[str] = None
