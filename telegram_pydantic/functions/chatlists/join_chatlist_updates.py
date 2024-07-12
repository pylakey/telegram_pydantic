from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JoinChatlistUpdates(BaseModel):
    """
    functions.chatlists.JoinChatlistUpdates
    ID: 0xe089f8f5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.JoinChatlistUpdates', 'JoinChatlistUpdates'] = pydantic.Field(
        'functions.chatlists.JoinChatlistUpdates',
        alias='_'
    )

    chatlist: "base.InputChatlist"
    peers: list["base.InputPeer"]
