from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UnregisterDevice(BaseModel):
    """
    functions.account.UnregisterDevice
    ID: 0x6a0d3206
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UnregisterDevice', 'UnregisterDevice'] = pydantic.Field(
        'functions.account.UnregisterDevice',
        alias='_'
    )

    token_type: int
    token: str
    other_uids: list[int]
