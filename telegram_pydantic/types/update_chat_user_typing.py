from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChatUserTyping(BaseModel):
    """
    types.UpdateChatUserTyping
    ID: 0x83487af0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChatUserTyping', 'UpdateChatUserTyping'] = pydantic.Field(
        'types.UpdateChatUserTyping',
        alias='_'
    )

    chat_id: int
    from_id: "base.Peer"
    action: "base.SendMessageAction"
