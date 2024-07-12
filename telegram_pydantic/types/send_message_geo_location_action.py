from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageGeoLocationAction(BaseModel):
    """
    types.SendMessageGeoLocationAction
    ID: 0x176f8ba1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageGeoLocationAction', 'SendMessageGeoLocationAction'] = pydantic.Field(
        'types.SendMessageGeoLocationAction',
        alias='_'
    )

