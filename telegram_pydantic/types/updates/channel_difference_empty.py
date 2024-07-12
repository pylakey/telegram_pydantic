from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelDifferenceEmpty(BaseModel):
    """
    types.updates.ChannelDifferenceEmpty
    ID: 0x3e11affb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.updates.ChannelDifferenceEmpty', 'ChannelDifferenceEmpty'] = pydantic.Field(
        'types.updates.ChannelDifferenceEmpty',
        alias='_'
    )

    pts: int
    final: typing.Optional[bool] = None
    timeout: typing.Optional[int] = None
