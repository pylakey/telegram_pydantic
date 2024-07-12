from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteChannel(BaseModel):
    """
    functions.channels.DeleteChannel
    ID: 0xc0111fe3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.DeleteChannel', 'DeleteChannel'] = pydantic.Field(
        'functions.channels.DeleteChannel',
        alias='_'
    )

    channel: "base.InputChannel"
