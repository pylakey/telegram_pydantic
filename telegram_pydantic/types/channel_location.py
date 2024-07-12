from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelLocation(BaseModel):
    """
    types.ChannelLocation
    ID: 0x209b82db
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelLocation', 'ChannelLocation'] = pydantic.Field(
        'types.ChannelLocation',
        alias='_'
    )

    geo_point: "base.GeoPoint"
    address: str
