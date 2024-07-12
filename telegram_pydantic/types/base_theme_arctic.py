from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BaseThemeArctic(BaseModel):
    """
    types.BaseThemeArctic
    ID: 0x5b11125a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BaseThemeArctic', 'BaseThemeArctic'] = pydantic.Field(
        'types.BaseThemeArctic',
        alias='_'
    )

