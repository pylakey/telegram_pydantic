from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDeviceLocked(BaseModel):
    """
    functions.account.UpdateDeviceLocked
    ID: 0x38df3532
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateDeviceLocked', 'UpdateDeviceLocked'] = pydantic.Field(
        'functions.account.UpdateDeviceLocked',
        alias='_'
    )

    period: int
