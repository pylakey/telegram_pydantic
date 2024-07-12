from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputGeoPoint(BaseModel):
    """
    types.InputGeoPoint
    ID: 0x48222faf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputGeoPoint', 'InputGeoPoint'] = pydantic.Field(
        'types.InputGeoPoint',
        alias='_'
    )

    lat: float
    long: float
    accuracy_radius: typing.Optional[int] = None
