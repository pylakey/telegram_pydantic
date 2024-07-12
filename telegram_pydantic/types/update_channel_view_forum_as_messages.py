from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannelViewForumAsMessages(BaseModel):
    """
    types.UpdateChannelViewForumAsMessages
    ID: 0x7b68920
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannelViewForumAsMessages', 'UpdateChannelViewForumAsMessages'] = pydantic.Field(
        'types.UpdateChannelViewForumAsMessages',
        alias='_'
    )

    channel_id: int
    enabled: bool
