from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Boost(BaseModel):
    """
    types.Boost
    ID: 0x2a1c8c71
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Boost', 'Boost'] = pydantic.Field(
        'types.Boost',
        alias='_'
    )

    id: str
    date: Datetime
    expires: Datetime
    gift: typing.Optional[bool] = None
    giveaway: typing.Optional[bool] = None
    unclaimed: typing.Optional[bool] = None
    user_id: typing.Optional[int] = None
    giveaway_msg_id: typing.Optional[int] = None
    used_gift_slug: typing.Optional[str] = None
    multiplier: typing.Optional[int] = None
