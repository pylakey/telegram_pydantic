from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadChannelDiscussionInbox(BaseModel):
    """
    types.UpdateReadChannelDiscussionInbox
    ID: 0xd6b19546
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadChannelDiscussionInbox', 'UpdateReadChannelDiscussionInbox'] = pydantic.Field(
        'types.UpdateReadChannelDiscussionInbox',
        alias='_'
    )

    channel_id: int
    top_msg_id: int
    read_max_id: int
    broadcast_id: typing.Optional[int] = None
    broadcast_post: typing.Optional[int] = None
