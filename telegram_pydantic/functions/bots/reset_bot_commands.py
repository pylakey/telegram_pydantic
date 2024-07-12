from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetBotCommands(BaseModel):
    """
    functions.bots.ResetBotCommands
    ID: 0x3d8de0f9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.ResetBotCommands', 'ResetBotCommands'] = pydantic.Field(
        'functions.bots.ResetBotCommands',
        alias='_'
    )

    scope: "base.BotCommandScope"
    lang_code: str
