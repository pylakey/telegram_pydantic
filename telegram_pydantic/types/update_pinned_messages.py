from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePinnedMessages(BaseModel):
    """
    types.UpdatePinnedMessages
    ID: 0xed85eab5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePinnedMessages', 'UpdatePinnedMessages'] = pydantic.Field(
        'types.UpdatePinnedMessages',
        alias='_'
    )

    peer: "base.Peer"
    messages: list[int]
    pts: int
    pts_count: int
    pinned: typing.Optional[bool] = None
