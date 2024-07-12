from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleAntiSpam(BaseModel):
    """
    functions.channels.ToggleAntiSpam
    ID: 0x68f3e4eb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleAntiSpam', 'ToggleAntiSpam'] = pydantic.Field(
        'functions.channels.ToggleAntiSpam',
        alias='_'
    )

    channel: "base.InputChannel"
    enabled: bool
