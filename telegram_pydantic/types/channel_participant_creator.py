from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantCreator(BaseModel):
    """
    types.ChannelParticipantCreator
    ID: 0x2fe601d3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantCreator', 'ChannelParticipantCreator'] = pydantic.Field(
        'types.ChannelParticipantCreator',
        alias='_'
    )

    user_id: int
    admin_rights: "base.ChatAdminRights"
    rank: typing.Optional[str] = None
