from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MaskCoords(BaseModel):
    """
    types.MaskCoords
    ID: 0xaed6dbb2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MaskCoords', 'MaskCoords'] = pydantic.Field(
        'types.MaskCoords',
        alias='_'
    )

    n: int
    x: float
    y: float
    zoom: float
