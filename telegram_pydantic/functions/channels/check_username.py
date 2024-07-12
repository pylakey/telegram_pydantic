from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckUsername(BaseModel):
    """
    functions.channels.CheckUsername
    ID: 0x10e6bd2c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.CheckUsername', 'CheckUsername'] = pydantic.Field(
        'functions.channels.CheckUsername',
        alias='_'
    )

    channel: "base.InputChannel"
    username: str
