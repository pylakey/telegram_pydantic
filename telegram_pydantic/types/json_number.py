from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JsonNumber(BaseModel):
    """
    types.JsonNumber
    ID: 0x2be0dfa4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.JsonNumber', 'JsonNumber'] = pydantic.Field(
        'types.JsonNumber',
        alias='_'
    )

    value: float
