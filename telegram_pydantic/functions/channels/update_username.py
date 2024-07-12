from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateUsername(BaseModel):
    """
    functions.channels.UpdateUsername
    ID: 0x3514b3de
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.UpdateUsername', 'UpdateUsername'] = pydantic.Field(
        'functions.channels.UpdateUsername',
        alias='_'
    )

    channel: "base.InputChannel"
    username: str
