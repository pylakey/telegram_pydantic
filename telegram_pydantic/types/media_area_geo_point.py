from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MediaAreaGeoPoint(BaseModel):
    """
    types.MediaAreaGeoPoint
    ID: 0xdf8b3b22
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MediaAreaGeoPoint', 'MediaAreaGeoPoint'] = pydantic.Field(
        'types.MediaAreaGeoPoint',
        alias='_'
    )

    coordinates: "base.MediaAreaCoordinates"
    geo: "base.GeoPoint"
