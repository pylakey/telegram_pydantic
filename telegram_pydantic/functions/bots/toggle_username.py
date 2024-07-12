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
    functions.bots.ToggleUsername
    ID: 0x53ca973
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.ToggleUsername', 'ToggleUsername'] = pydantic.Field(
        'functions.bots.ToggleUsername',
        alias='_'
    )

    bot: "base.InputUser"
    username: str
    active: bool
