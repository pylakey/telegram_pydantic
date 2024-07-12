from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GeoPoint(BaseModel):
    """
    types.GeoPoint
    ID: 0xb2a2f663
    Layer: 181
    """
    QUALNAME: typing.Literal['types.GeoPoint', 'GeoPoint'] = pydantic.Field(
        'types.GeoPoint',
        alias='_'
    )

    long: float
    lat: float
    access_hash: int
    accuracy_radius: typing.Optional[int] = None
