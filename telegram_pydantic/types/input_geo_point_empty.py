from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputGeoPointEmpty(BaseModel):
    """
    types.InputGeoPointEmpty
    ID: 0xe4c123d6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputGeoPointEmpty', 'InputGeoPointEmpty'] = pydantic.Field(
        'types.InputGeoPointEmpty',
        alias='_'
    )

