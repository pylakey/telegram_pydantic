from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ClearSavedInfo(BaseModel):
    """
    functions.payments.ClearSavedInfo
    ID: 0xd83d70c1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.ClearSavedInfo', 'ClearSavedInfo'] = pydantic.Field(
        'functions.payments.ClearSavedInfo',
        alias='_'
    )

    credentials: typing.Optional[bool] = None
    info: typing.Optional[bool] = None
