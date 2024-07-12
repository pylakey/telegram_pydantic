from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotCommands(BaseModel):
    """
    types.UpdateBotCommands
    ID: 0x4d712f2e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotCommands', 'UpdateBotCommands'] = pydantic.Field(
        'types.UpdateBotCommands',
        alias='_'
    )

    peer: "base.Peer"
    bot_id: int
    commands: list["base.BotCommand"]
