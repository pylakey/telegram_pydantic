from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadHistory(BaseModel):
    """
    functions.channels.ReadHistory
    ID: 0xcc104937
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ReadHistory', 'ReadHistory'] = pydantic.Field(
        'functions.channels.ReadHistory',
        alias='_'
    )

    channel: "base.InputChannel"
    max_id: int
