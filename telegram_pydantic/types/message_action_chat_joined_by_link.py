from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChatJoinedByLink(BaseModel):
    """
    types.MessageActionChatJoinedByLink
    ID: 0x31224c3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChatJoinedByLink', 'MessageActionChatJoinedByLink'] = pydantic.Field(
        'types.MessageActionChatJoinedByLink',
        alias='_'
    )

    inviter_id: int
