from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBotMenuButton(BaseModel):
    """
    functions.bots.SetBotMenuButton
    ID: 0x4504d54f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.SetBotMenuButton', 'SetBotMenuButton'] = pydantic.Field(
        'functions.bots.SetBotMenuButton',
        alias='_'
    )

    user_id: "base.InputUser"
    button: "base.BotMenuButton"
