from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadChannelDiscussionOutbox(BaseModel):
    """
    types.UpdateReadChannelDiscussionOutbox
    ID: 0x695c9e7c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadChannelDiscussionOutbox', 'UpdateReadChannelDiscussionOutbox'] = pydantic.Field(
        'types.UpdateReadChannelDiscussionOutbox',
        alias='_'
    )

    channel_id: int
    top_msg_id: int
    read_max_id: int
