from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantJoin(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantJoin
    ID: 0x183040d3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantJoin', 'ChannelAdminLogEventActionParticipantJoin'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantJoin',
        alias='_'
    )

