from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantToggleAdmin(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantToggleAdmin
    ID: 0xd5676710
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantToggleAdmin', 'ChannelAdminLogEventActionParticipantToggleAdmin'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantToggleAdmin',
        alias='_'
    )

    prev_participant: "base.ChannelParticipant"
    new_participant: "base.ChannelParticipant"
