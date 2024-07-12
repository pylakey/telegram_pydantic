from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleJoinRequest(BaseModel):
    """
    functions.channels.ToggleJoinRequest
    ID: 0x4c2985b6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleJoinRequest', 'ToggleJoinRequest'] = pydantic.Field(
        'functions.channels.ToggleJoinRequest',
        alias='_'
    )

    channel: "base.InputChannel"
    enabled: bool
