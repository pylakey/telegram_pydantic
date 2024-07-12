from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantToggleBan(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantToggleBan
    ID: 0xe6d83d7e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantToggleBan', 'ChannelAdminLogEventActionParticipantToggleBan'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantToggleBan',
        alias='_'
    )

    prev_participant: "base.ChannelParticipant"
    new_participant: "base.ChannelParticipant"
