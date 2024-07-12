from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotMenuButtonCommands(BaseModel):
    """
    types.BotMenuButtonCommands
    ID: 0x4258c205
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotMenuButtonCommands', 'BotMenuButtonCommands'] = pydantic.Field(
        'types.BotMenuButtonCommands',
        alias='_'
    )

