from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JoinChatlistInvite(BaseModel):
    """
    functions.chatlists.JoinChatlistInvite
    ID: 0xa6b1e39a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.JoinChatlistInvite', 'JoinChatlistInvite'] = pydantic.Field(
        'functions.chatlists.JoinChatlistInvite',
        alias='_'
    )

    slug: str
    peers: list["base.InputPeer"]
