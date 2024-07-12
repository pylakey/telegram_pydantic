from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantVolume(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantVolume
    ID: 0x3e7f6847
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantVolume', 'ChannelAdminLogEventActionParticipantVolume'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantVolume',
        alias='_'
    )

    participant: "base.GroupCallParticipant"
