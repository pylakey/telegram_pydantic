from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaAreaVenue(BaseModel):
    """
    types.InputMediaAreaVenue
    ID: 0xb282217f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaAreaVenue', 'InputMediaAreaVenue'] = pydantic.Field(
        'types.InputMediaAreaVenue',
        alias='_'
    )

    coordinates: "base.MediaAreaCoordinates"
    query_id: int
    result_id: str
