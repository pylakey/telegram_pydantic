from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotInfo(BaseModel):
    """
    types.bots.BotInfo
    ID: 0xe8a775b0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.bots.BotInfo', 'BotInfo'] = pydantic.Field(
        'types.bots.BotInfo',
        alias='_'
    )

    name: str
    about: str
    description: str
