from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotMenuButton(BaseModel):
    """
    types.UpdateBotMenuButton
    ID: 0x14b85813
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotMenuButton', 'UpdateBotMenuButton'] = pydantic.Field(
        'types.UpdateBotMenuButton',
        alias='_'
    )

    bot_id: int
    button: "base.BotMenuButton"
