from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JoinChannel(BaseModel):
    """
    functions.channels.JoinChannel
    ID: 0x24b524c5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.JoinChannel', 'JoinChannel'] = pydantic.Field(
        'functions.channels.JoinChannel',
        alias='_'
    )

    channel: "base.InputChannel"
