from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannelTooLong(BaseModel):
    """
    types.UpdateChannelTooLong
    ID: 0x108d941f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannelTooLong', 'UpdateChannelTooLong'] = pydantic.Field(
        'types.UpdateChannelTooLong',
        alias='_'
    )

    channel_id: int
    pts: typing.Optional[int] = None
