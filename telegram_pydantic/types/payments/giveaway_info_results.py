from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GiveawayInfoResults(BaseModel):
    """
    types.payments.GiveawayInfoResults
    ID: 0xcd5570
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.GiveawayInfoResults', 'GiveawayInfoResults'] = pydantic.Field(
        'types.payments.GiveawayInfoResults',
        alias='_'
    )

    start_date: Datetime
    finish_date: Datetime
    winners_count: int
    activated_count: int
    winner: typing.Optional[bool] = None
    refunded: typing.Optional[bool] = None
    gift_code_slug: typing.Optional[str] = None
