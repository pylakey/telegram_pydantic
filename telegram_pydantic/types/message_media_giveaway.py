from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaGiveaway(BaseModel):
    """
    types.MessageMediaGiveaway
    ID: 0xdaad85b0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaGiveaway', 'MessageMediaGiveaway'] = pydantic.Field(
        'types.MessageMediaGiveaway',
        alias='_'
    )

    channels: list[int]
    quantity: int
    months: int
    until_date: Datetime
    only_new_subscribers: typing.Optional[bool] = None
    winners_are_visible: typing.Optional[bool] = None
    countries_iso2: typing.Optional[list[str]] = None
    prize_description: typing.Optional[str] = None
