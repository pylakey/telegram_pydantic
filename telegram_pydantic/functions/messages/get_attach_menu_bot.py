from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAttachMenuBot(BaseModel):
    """
    functions.messages.GetAttachMenuBot
    ID: 0x77216192
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetAttachMenuBot', 'GetAttachMenuBot'] = pydantic.Field(
        'functions.messages.GetAttachMenuBot',
        alias='_'
    )

    bot: "base.InputUser"
