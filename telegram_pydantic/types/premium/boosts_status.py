from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BoostsStatus(BaseModel):
    """
    types.premium.BoostsStatus
    ID: 0x4959427a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.premium.BoostsStatus', 'BoostsStatus'] = pydantic.Field(
        'types.premium.BoostsStatus',
        alias='_'
    )

    level: int
    current_level_boosts: int
    boosts: int
    boost_url: str
    my_boost: typing.Optional[bool] = None
    gift_boosts: typing.Optional[int] = None
    next_level_boosts: typing.Optional[int] = None
    premium_audience: typing.Optional["base.StatsPercentValue"] = None
    prepaid_giveaways: typing.Optional[list["base.PrepaidGiveaway"]] = None
    my_boost_slots: typing.Optional[list[int]] = None
