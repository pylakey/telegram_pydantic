from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatesCombined(BaseModel):
    """
    types.UpdatesCombined
    ID: 0x725b04c3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatesCombined', 'UpdatesCombined'] = pydantic.Field(
        'types.UpdatesCombined',
        alias='_'
    )

    updates: list["base.Update"]
    users: list["base.User"]
    chats: list["base.Chat"]
    date: Datetime
    seq_start: int
    seq: int
