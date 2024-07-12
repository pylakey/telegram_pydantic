from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditLocation(BaseModel):
    """
    functions.channels.EditLocation
    ID: 0x58e63f6d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.EditLocation', 'EditLocation'] = pydantic.Field(
        'functions.channels.EditLocation',
        alias='_'
    )

    channel: "base.InputChannel"
    geo_point: "base.InputGeoPoint"
    address: str
