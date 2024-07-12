from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotCommand(BaseModel):
    """
    types.BotCommand
    ID: 0xc27ac8c7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotCommand', 'BotCommand'] = pydantic.Field(
        'types.BotCommand',
        alias='_'
    )

    command: str
    description: str
