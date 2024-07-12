from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FinishTakeoutSession(BaseModel):
    """
    functions.account.FinishTakeoutSession
    ID: 0x1d2652ee
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.FinishTakeoutSession', 'FinishTakeoutSession'] = pydantic.Field(
        'functions.account.FinishTakeoutSession',
        alias='_'
    )

    success: typing.Optional[bool] = None
