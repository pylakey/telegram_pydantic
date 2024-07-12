from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChats(BaseModel):
    """
    functions.messages.GetChats
    ID: 0x49e9528f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetChats', 'GetChats'] = pydantic.Field(
        'functions.messages.GetChats',
        alias='_'
    )

    id: list[int]
