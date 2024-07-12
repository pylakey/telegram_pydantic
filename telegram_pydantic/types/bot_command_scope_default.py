from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotCommandScopeDefault(BaseModel):
    """
    types.BotCommandScopeDefault
    ID: 0x2f6cb2ab
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotCommandScopeDefault', 'BotCommandScopeDefault'] = pydantic.Field(
        'types.BotCommandScopeDefault',
        alias='_'
    )

