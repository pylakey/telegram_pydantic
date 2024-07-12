from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantLeft(BaseModel):
    """
    types.ChannelParticipantLeft
    ID: 0x1b03f006
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantLeft', 'ChannelParticipantLeft'] = pydantic.Field(
        'types.ChannelParticipantLeft',
        alias='_'
    )

    peer: "base.Peer"
