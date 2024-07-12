from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteMessages(BaseModel):
    """
    functions.channels.DeleteMessages
    ID: 0x84c1fd4e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.DeleteMessages', 'DeleteMessages'] = pydantic.Field(
        'functions.channels.DeleteMessages',
        alias='_'
    )

    channel: "base.InputChannel"
    id: list[int]
