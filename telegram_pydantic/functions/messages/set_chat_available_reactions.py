from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetChatAvailableReactions(BaseModel):
    """
    functions.messages.SetChatAvailableReactions
    ID: 0x5a150bd4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetChatAvailableReactions', 'SetChatAvailableReactions'] = pydantic.Field(
        'functions.messages.SetChatAvailableReactions',
        alias='_'
    )

    peer: "base.InputPeer"
    available_reactions: "base.ChatReactions"
    reactions_limit: typing.Optional[int] = None
