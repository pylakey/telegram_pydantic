from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantBanned(BaseModel):
    """
    types.ChannelParticipantBanned
    ID: 0x6df8014e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantBanned', 'ChannelParticipantBanned'] = pydantic.Field(
        'types.ChannelParticipantBanned',
        alias='_'
    )

    peer: "base.Peer"
    kicked_by: int
    date: Datetime
    banned_rights: "base.ChatBannedRights"
    left: typing.Optional[bool] = None
