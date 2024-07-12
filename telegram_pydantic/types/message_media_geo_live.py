from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaGeoLive(BaseModel):
    """
    types.MessageMediaGeoLive
    ID: 0xb940c666
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaGeoLive', 'MessageMediaGeoLive'] = pydantic.Field(
        'types.MessageMediaGeoLive',
        alias='_'
    )

    geo: "base.GeoPoint"
    period: int
    heading: typing.Optional[int] = None
    proximity_notification_radius: typing.Optional[int] = None
