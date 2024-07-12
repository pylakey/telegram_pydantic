from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TogglePreHistoryHidden(BaseModel):
    """
    functions.channels.TogglePreHistoryHidden
    ID: 0xeabbb94c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.TogglePreHistoryHidden', 'TogglePreHistoryHidden'] = pydantic.Field(
        'functions.channels.TogglePreHistoryHidden',
        alias='_'
    )

    channel: "base.InputChannel"
    enabled: bool
