from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MyBoost(BaseModel):
    """
    types.MyBoost
    ID: 0xc448415c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MyBoost', 'MyBoost'] = pydantic.Field(
        'types.MyBoost',
        alias='_'
    )

    slot: int
    date: Datetime
    expires: Datetime
    peer: typing.Optional["base.Peer"] = None
    cooldown_until_date: typing.Optional[Datetime] = None
