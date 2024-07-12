from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannelReadMessagesContents(BaseModel):
    """
    types.UpdateChannelReadMessagesContents
    ID: 0xea29055d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannelReadMessagesContents', 'UpdateChannelReadMessagesContents'] = pydantic.Field(
        'types.UpdateChannelReadMessagesContents',
        alias='_'
    )

    channel_id: int
    messages: list[int]
    top_msg_id: typing.Optional[int] = None
