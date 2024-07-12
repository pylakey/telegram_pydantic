from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantMute(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantMute
    ID: 0xf92424d2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantMute', 'ChannelAdminLogEventActionParticipantMute'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantMute',
        alias='_'
    )

    participant: "base.GroupCallParticipant"
