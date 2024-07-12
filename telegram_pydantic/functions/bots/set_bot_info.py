from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBotInfo(BaseModel):
    """
    functions.bots.SetBotInfo
    ID: 0x10cf3123
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.SetBotInfo', 'SetBotInfo'] = pydantic.Field(
        'functions.bots.SetBotInfo',
        alias='_'
    )

    lang_code: str
    bot: typing.Optional["base.InputUser"] = None
    name: typing.Optional[str] = None
    about: typing.Optional[str] = None
    description: typing.Optional[str] = None
