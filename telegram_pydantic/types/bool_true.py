from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BoolTrue(BaseModel):
    """
    types.BoolTrue
    ID: 0x997275b5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BoolTrue', 'BoolTrue'] = pydantic.Field(
        'types.BoolTrue',
        alias='_'
    )

