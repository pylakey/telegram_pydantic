from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaGeo(BaseModel):
    """
    types.MessageMediaGeo
    ID: 0x56e0d474
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaGeo', 'MessageMediaGeo'] = pydantic.Field(
        'types.MessageMediaGeo',
        alias='_'
    )

    geo: "base.GeoPoint"
