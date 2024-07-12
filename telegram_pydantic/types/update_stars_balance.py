from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateStarsBalance(BaseModel):
    """
    types.UpdateStarsBalance
    ID: 0xfb85198
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateStarsBalance', 'UpdateStarsBalance'] = pydantic.Field(
        'types.UpdateStarsBalance',
        alias='_'
    )

    balance: int
