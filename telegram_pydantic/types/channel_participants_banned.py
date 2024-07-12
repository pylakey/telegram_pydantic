from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantsBanned(BaseModel):
    """
    types.ChannelParticipantsBanned
    ID: 0x1427a5e1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantsBanned', 'ChannelParticipantsBanned'] = pydantic.Field(
        'types.ChannelParticipantsBanned',
        alias='_'
    )

    q: str
