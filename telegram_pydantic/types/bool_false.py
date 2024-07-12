from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BoolFalse(BaseModel):
    """
    types.BoolFalse
    ID: 0xbc799737
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BoolFalse', 'BoolFalse'] = pydantic.Field(
        'types.BoolFalse',
        alias='_'
    )

