from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MediaAreaVenue(BaseModel):
    """
    types.MediaAreaVenue
    ID: 0xbe82db9c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MediaAreaVenue', 'MediaAreaVenue'] = pydantic.Field(
        'types.MediaAreaVenue',
        alias='_'
    )

    coordinates: "base.MediaAreaCoordinates"
    geo: "base.GeoPoint"
    title: str
    address: str
    provider: str
    venue_id: str
    venue_type: str
