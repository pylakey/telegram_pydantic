from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDhConfig(BaseModel):
    """
    functions.messages.GetDhConfig
    ID: 0x26cf8950
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDhConfig', 'GetDhConfig'] = pydantic.Field(
        'functions.messages.GetDhConfig',
        alias='_'
    )

    version: int
    random_length: int
