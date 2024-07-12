from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PostInteractionCountersMessage(BaseModel):
    """
    types.PostInteractionCountersMessage
    ID: 0xe7058e7f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PostInteractionCountersMessage', 'PostInteractionCountersMessage'] = pydantic.Field(
        'types.PostInteractionCountersMessage',
        alias='_'
    )

    msg_id: int
    views: int
    forwards: int
    reactions: int
