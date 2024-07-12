from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LeaveChannel(BaseModel):
    """
    functions.channels.LeaveChannel
    ID: 0xf836aa95
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.LeaveChannel', 'LeaveChannel'] = pydantic.Field(
        'functions.channels.LeaveChannel',
        alias='_'
    )

    channel: "base.InputChannel"
