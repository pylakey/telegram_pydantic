from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerChat(BaseModel):
    """
    types.PeerChat
    ID: 0x36c6019a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerChat', 'PeerChat'] = pydantic.Field(
        'types.PeerChat',
        alias='_'
    )

    chat_id: int
