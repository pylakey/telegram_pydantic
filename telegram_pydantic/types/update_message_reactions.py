from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateMessageReactions(BaseModel):
    """
    types.UpdateMessageReactions
    ID: 0x5e1b3cb8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateMessageReactions', 'UpdateMessageReactions'] = pydantic.Field(
        'types.UpdateMessageReactions',
        alias='_'
    )

    peer: "base.Peer"
    msg_id: int
    reactions: "base.MessageReactions"
    top_msg_id: typing.Optional[int] = None
