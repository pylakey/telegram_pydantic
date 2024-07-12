from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionRequestedPeer(BaseModel):
    """
    types.MessageActionRequestedPeer
    ID: 0x31518e9b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionRequestedPeer', 'MessageActionRequestedPeer'] = pydantic.Field(
        'types.MessageActionRequestedPeer',
        alias='_'
    )

    button_id: int
    peers: list["base.Peer"]
