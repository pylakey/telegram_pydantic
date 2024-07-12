from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannel(BaseModel):
    """
    types.UpdateChannel
    ID: 0x635b4c09
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannel', 'UpdateChannel'] = pydantic.Field(
        'types.UpdateChannel',
        alias='_'
    )

    channel_id: int
