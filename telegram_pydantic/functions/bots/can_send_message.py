from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CanSendMessage(BaseModel):
    """
    functions.bots.CanSendMessage
    ID: 0x1359f4e6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.CanSendMessage', 'CanSendMessage'] = pydantic.Field(
        'functions.bots.CanSendMessage',
        alias='_'
    )

    bot: "base.InputUser"
