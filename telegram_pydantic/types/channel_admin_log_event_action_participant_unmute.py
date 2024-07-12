from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantUnmute(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantUnmute
    ID: 0xe64429c0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantUnmute', 'ChannelAdminLogEventActionParticipantUnmute'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantUnmute',
        alias='_'
    )

    participant: "base.GroupCallParticipant"
