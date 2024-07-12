from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetAccountTTL(BaseModel):
    """
    functions.account.SetAccountTTL
    ID: 0x2442485e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SetAccountTTL', 'SetAccountTTL'] = pydantic.Field(
        'functions.account.SetAccountTTL',
        alias='_'
    )

    ttl: "base.AccountDaysTTL"
