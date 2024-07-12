from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaVenue(BaseModel):
    """
    types.MessageMediaVenue
    ID: 0x2ec0533f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaVenue', 'MessageMediaVenue'] = pydantic.Field(
        'types.MessageMediaVenue',
        alias='_'
    )

    geo: "base.GeoPoint"
    title: str
    address: str
    provider: str
    venue_id: str
    venue_type: str
