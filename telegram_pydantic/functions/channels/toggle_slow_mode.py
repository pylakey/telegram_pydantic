from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleSlowMode(BaseModel):
    """
    functions.channels.ToggleSlowMode
    ID: 0xedd49ef0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleSlowMode', 'ToggleSlowMode'] = pydantic.Field(
        'functions.channels.ToggleSlowMode',
        alias='_'
    )

    channel: "base.InputChannel"
    seconds: int
