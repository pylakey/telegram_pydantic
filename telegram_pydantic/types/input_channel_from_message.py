from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputChannelFromMessage(BaseModel):
    """
    types.InputChannelFromMessage
    ID: 0x5b934f9d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputChannelFromMessage', 'InputChannelFromMessage'] = pydantic.Field(
        'types.InputChannelFromMessage',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    channel_id: int
