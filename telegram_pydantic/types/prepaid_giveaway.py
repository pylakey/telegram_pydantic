from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrepaidGiveaway(BaseModel):
    """
    types.PrepaidGiveaway
    ID: 0xb2539d54
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrepaidGiveaway', 'PrepaidGiveaway'] = pydantic.Field(
        'types.PrepaidGiveaway',
        alias='_'
    )

    id: int
    months: int
    quantity: int
    date: Datetime
