from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleBotInAttachMenu(BaseModel):
    """
    functions.messages.ToggleBotInAttachMenu
    ID: 0x69f59d69
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ToggleBotInAttachMenu', 'ToggleBotInAttachMenu'] = pydantic.Field(
        'functions.messages.ToggleBotInAttachMenu',
        alias='_'
    )

    bot: "base.InputUser"
    enabled: bool
    write_allowed: typing.Optional[bool] = None
