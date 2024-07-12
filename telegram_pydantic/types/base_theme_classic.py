from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BaseThemeClassic(BaseModel):
    """
    types.BaseThemeClassic
    ID: 0xc3a12462
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BaseThemeClassic', 'BaseThemeClassic'] = pydantic.Field(
        'types.BaseThemeClassic',
        alias='_'
    )

