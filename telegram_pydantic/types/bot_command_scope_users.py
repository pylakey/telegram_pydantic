from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotCommandScopeUsers(BaseModel):
    """
    types.BotCommandScopeUsers
    ID: 0x3c4f04d8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotCommandScopeUsers', 'BotCommandScopeUsers'] = pydantic.Field(
        'types.BotCommandScopeUsers',
        alias='_'
    )

