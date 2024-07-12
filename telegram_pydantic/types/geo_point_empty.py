from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GeoPointEmpty(BaseModel):
    """
    types.GeoPointEmpty
    ID: 0x1117dd5f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.GeoPointEmpty', 'GeoPointEmpty'] = pydantic.Field(
        'types.GeoPointEmpty',
        alias='_'
    )

