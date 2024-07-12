from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleJoinToSend(BaseModel):
    """
    functions.channels.ToggleJoinToSend
    ID: 0xe4cb9580
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleJoinToSend', 'ToggleJoinToSend'] = pydantic.Field(
        'functions.channels.ToggleJoinToSend',
        alias='_'
    )

    channel: "base.InputChannel"
    enabled: bool
