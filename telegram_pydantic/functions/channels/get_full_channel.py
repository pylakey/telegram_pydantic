from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetFullChannel(BaseModel):
    """
    functions.channels.GetFullChannel
    ID: 0x8736a09
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetFullChannel', 'GetFullChannel'] = pydantic.Field(
        'functions.channels.GetFullChannel',
        alias='_'
    )

    channel: "base.InputChannel"
