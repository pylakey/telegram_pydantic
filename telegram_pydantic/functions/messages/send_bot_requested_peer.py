from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendBotRequestedPeer(BaseModel):
    """
    functions.messages.SendBotRequestedPeer
    ID: 0x91b2d060
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendBotRequestedPeer', 'SendBotRequestedPeer'] = pydantic.Field(
        'functions.messages.SendBotRequestedPeer',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    button_id: int
    requested_peers: list["base.InputPeer"]
