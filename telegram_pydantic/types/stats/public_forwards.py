from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PublicForwards(BaseModel):
    """
    types.stats.PublicForwards
    ID: 0x93037e20
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stats.PublicForwards', 'PublicForwards'] = pydantic.Field(
        'types.stats.PublicForwards',
        alias='_'
    )

    count: int
    forwards: list["base.PublicForward"]
    chats: list["base.Chat"]
    users: list["base.User"]
    next_offset: typing.Optional[str] = None
