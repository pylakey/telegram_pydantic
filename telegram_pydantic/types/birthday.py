from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Birthday(BaseModel):
    """
    types.Birthday
    ID: 0x6c8e1e06
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Birthday', 'Birthday'] = pydantic.Field(
        'types.Birthday',
        alias='_'
    )

    day: int
    month: int
    year: typing.Optional[int] = None
