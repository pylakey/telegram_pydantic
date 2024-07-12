from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaVenue(BaseModel):
    """
    types.InputMediaVenue
    ID: 0xc13d1c11
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaVenue', 'InputMediaVenue'] = pydantic.Field(
        'types.InputMediaVenue',
        alias='_'
    )

    geo_point: "base.InputGeoPoint"
    title: str
    address: str
    provider: str
    venue_id: str
    venue_type: str
