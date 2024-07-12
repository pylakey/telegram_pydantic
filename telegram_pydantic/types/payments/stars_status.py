from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StarsStatus(BaseModel):
    """
    types.payments.StarsStatus
    ID: 0x8cf4ee60
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.StarsStatus', 'StarsStatus'] = pydantic.Field(
        'types.payments.StarsStatus',
        alias='_'
    )

    balance: int
    history: list["base.StarsTransaction"]
    chats: list["base.Chat"]
    users: list["base.User"]
    next_offset: typing.Optional[str] = None
