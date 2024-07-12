from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaGeoPoint(BaseModel):
    """
    types.InputMediaGeoPoint
    ID: 0xf9c44144
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaGeoPoint', 'InputMediaGeoPoint'] = pydantic.Field(
        'types.InputMediaGeoPoint',
        alias='_'
    )

    geo_point: "base.InputGeoPoint"
