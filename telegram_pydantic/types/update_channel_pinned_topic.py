from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannelPinnedTopic(BaseModel):
    """
    types.UpdateChannelPinnedTopic
    ID: 0x192efbe3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannelPinnedTopic', 'UpdateChannelPinnedTopic'] = pydantic.Field(
        'types.UpdateChannelPinnedTopic',
        alias='_'
    )

    channel_id: int
    topic_id: int
    pinned: typing.Optional[bool] = None
