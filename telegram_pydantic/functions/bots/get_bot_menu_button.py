from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBotMenuButton(BaseModel):
    """
    functions.bots.GetBotMenuButton
    ID: 0x9c60eb28
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.GetBotMenuButton', 'GetBotMenuButton'] = pydantic.Field(
        'functions.bots.GetBotMenuButton',
        alias='_'
    )

    user_id: "base.InputUser"
