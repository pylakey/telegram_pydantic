from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePinnedChannelMessages(BaseModel):
    """
    types.UpdatePinnedChannelMessages
    ID: 0x5bb98608
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePinnedChannelMessages', 'UpdatePinnedChannelMessages'] = pydantic.Field(
        'types.UpdatePinnedChannelMessages',
        alias='_'
    )

    channel_id: int
    messages: list[int]
    pts: int
    pts_count: int
    pinned: typing.Optional[bool] = None
