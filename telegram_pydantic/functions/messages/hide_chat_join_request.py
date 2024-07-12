from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HideChatJoinRequest(BaseModel):
    """
    functions.messages.HideChatJoinRequest
    ID: 0x7fe7e815
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.HideChatJoinRequest', 'HideChatJoinRequest'] = pydantic.Field(
        'functions.messages.HideChatJoinRequest',
        alias='_'
    )

    peer: "base.InputPeer"
    user_id: "base.InputUser"
    approved: typing.Optional[bool] = None
