from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleUsername(BaseModel):
    """
    functions.channels.ToggleUsername
    ID: 0x50f24105
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleUsername', 'ToggleUsername'] = pydantic.Field(
        'functions.channels.ToggleUsername',
        alias='_'
    )

    channel: "base.InputChannel"
    username: str
    active: bool
