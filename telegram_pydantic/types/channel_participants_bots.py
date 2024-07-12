from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantsBots(BaseModel):
    """
    types.ChannelParticipantsBots
    ID: 0xb0d1865b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantsBots', 'ChannelParticipantsBots'] = pydantic.Field(
        'types.ChannelParticipantsBots',
        alias='_'
    )

