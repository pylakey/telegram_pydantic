from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaGiveawayResults(BaseModel):
    """
    types.MessageMediaGiveawayResults
    ID: 0xc6991068
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaGiveawayResults', 'MessageMediaGiveawayResults'] = pydantic.Field(
        'types.MessageMediaGiveawayResults',
        alias='_'
    )

    channel_id: int
    launch_msg_id: int
    winners_count: int
    unclaimed_count: int
    winners: list[int]
    months: int
    until_date: Datetime
    only_new_subscribers: typing.Optional[bool] = None
    refunded: typing.Optional[bool] = None
    additional_peers_count: typing.Optional[int] = None
    prize_description: typing.Optional[str] = None
