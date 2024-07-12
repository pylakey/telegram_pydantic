from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantsContacts(BaseModel):
    """
    types.ChannelParticipantsContacts
    ID: 0xbb6ae88d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantsContacts', 'ChannelParticipantsContacts'] = pydantic.Field(
        'types.ChannelParticipantsContacts',
        alias='_'
    )

    q: str
