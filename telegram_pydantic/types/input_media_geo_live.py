from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaGeoLive(BaseModel):
    """
    types.InputMediaGeoLive
    ID: 0x971fa843
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaGeoLive', 'InputMediaGeoLive'] = pydantic.Field(
        'types.InputMediaGeoLive',
        alias='_'
    )

    geo_point: "base.InputGeoPoint"
    stopped: typing.Optional[bool] = None
    heading: typing.Optional[int] = None
    period: typing.Optional[int] = None
    proximity_notification_radius: typing.Optional[int] = None
