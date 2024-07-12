from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotCommandScopeChats(BaseModel):
    """
    types.BotCommandScopeChats
    ID: 0x6fe1a881
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotCommandScopeChats', 'BotCommandScopeChats'] = pydantic.Field(
        'types.BotCommandScopeChats',
        alias='_'
    )

