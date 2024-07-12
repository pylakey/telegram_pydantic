from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantLeave(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantLeave
    ID: 0xf89777f2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantLeave', 'ChannelAdminLogEventActionParticipantLeave'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantLeave',
        alias='_'
    )

