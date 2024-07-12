from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantsRecent(BaseModel):
    """
    types.ChannelParticipantsRecent
    ID: 0xde3f3c79
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantsRecent', 'ChannelParticipantsRecent'] = pydantic.Field(
        'types.ChannelParticipantsRecent',
        alias='_'
    )

