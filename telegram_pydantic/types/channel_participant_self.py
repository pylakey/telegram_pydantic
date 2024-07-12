from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantSelf(BaseModel):
    """
    types.ChannelParticipantSelf
    ID: 0x35a8bfa7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantSelf', 'ChannelParticipantSelf'] = pydantic.Field(
        'types.ChannelParticipantSelf',
        alias='_'
    )

    user_id: int
    inviter_id: int
    date: Datetime
    via_request: typing.Optional[bool] = None
