from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotStopped(BaseModel):
    """
    types.UpdateBotStopped
    ID: 0xc4870a49
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotStopped', 'UpdateBotStopped'] = pydantic.Field(
        'types.UpdateBotStopped',
        alias='_'
    )

    user_id: int
    date: Datetime
    stopped: bool
    qts: int
