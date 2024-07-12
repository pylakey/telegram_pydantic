from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AllowSendMessage(BaseModel):
    """
    functions.bots.AllowSendMessage
    ID: 0xf132e3ef
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.AllowSendMessage', 'AllowSendMessage'] = pydantic.Field(
        'functions.bots.AllowSendMessage',
        alias='_'
    )

    bot: "base.InputUser"
