from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DhConfig(BaseModel):
    """
    types.messages.DhConfig
    ID: 0x2c221edd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.DhConfig', 'DhConfig'] = pydantic.Field(
        'types.messages.DhConfig',
        alias='_'
    )

    g: int
    p: Bytes
    version: int
    random: Bytes
