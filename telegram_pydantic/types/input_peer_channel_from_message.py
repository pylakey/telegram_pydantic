from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPeerChannelFromMessage(BaseModel):
    """
    types.InputPeerChannelFromMessage
    ID: 0xbd2a0840
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPeerChannelFromMessage', 'InputPeerChannelFromMessage'] = pydantic.Field(
        'types.InputPeerChannelFromMessage',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    channel_id: int
