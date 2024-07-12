from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DataJSON(BaseModel):
    """
    types.DataJSON
    ID: 0x7d748d04
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DataJSON', 'DataJSON'] = pydantic.Field(
        'types.DataJSON',
        alias='_'
    )

    data: str
