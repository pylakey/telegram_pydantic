from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputChannel(BaseModel):
    """
    types.InputChannel
    ID: 0xf35aec28
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputChannel', 'InputChannel'] = pydantic.Field(
        'types.InputChannel',
        alias='_'
    )

    channel_id: int
    access_hash: int
