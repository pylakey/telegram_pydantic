from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPeerChat(BaseModel):
    """
    types.InputPeerChat
    ID: 0x35a95cb9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPeerChat', 'InputPeerChat'] = pydantic.Field(
        'types.InputPeerChat',
        alias='_'
    )

    chat_id: int
