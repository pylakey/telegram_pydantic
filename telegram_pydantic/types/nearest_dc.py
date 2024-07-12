from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NearestDc(BaseModel):
    """
    types.NearestDc
    ID: 0x8e1a1775
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NearestDc', 'NearestDc'] = pydantic.Field(
        'types.NearestDc',
        alias='_'
    )

    country: str
    this_dc: int
    nearest_dc: int
