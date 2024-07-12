from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetLocated(BaseModel):
    """
    functions.contacts.GetLocated
    ID: 0xd348bc44
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.GetLocated', 'GetLocated'] = pydantic.Field(
        'functions.contacts.GetLocated',
        alias='_'
    )

    geo_point: "base.InputGeoPoint"
    background: typing.Optional[bool] = None
    self_expires: typing.Optional[int] = None
