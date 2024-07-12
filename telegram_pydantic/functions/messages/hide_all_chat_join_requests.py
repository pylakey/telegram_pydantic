from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HideAllChatJoinRequests(BaseModel):
    """
    functions.messages.HideAllChatJoinRequests
    ID: 0xe085f4ea
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.HideAllChatJoinRequests', 'HideAllChatJoinRequests'] = pydantic.Field(
        'functions.messages.HideAllChatJoinRequests',
        alias='_'
    )

    peer: "base.InputPeer"
    approved: typing.Optional[bool] = None
    link: typing.Optional[str] = None
