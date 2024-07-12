from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantsSearch(BaseModel):
    """
    types.ChannelParticipantsSearch
    ID: 0x656ac4b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantsSearch', 'ChannelParticipantsSearch'] = pydantic.Field(
        'types.ChannelParticipantsSearch',
        alias='_'
    )

    q: str
