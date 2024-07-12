from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadChannelInbox(BaseModel):
    """
    types.UpdateReadChannelInbox
    ID: 0x922e6e10
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadChannelInbox', 'UpdateReadChannelInbox'] = pydantic.Field(
        'types.UpdateReadChannelInbox',
        alias='_'
    )

    channel_id: int
    max_id: int
    still_unread_count: int
    pts: int
    folder_id: typing.Optional[int] = None
