from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEmpty(BaseModel):
    """
    types.MessageEmpty
    ID: 0x90a6ca84
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEmpty', 'MessageEmpty'] = pydantic.Field(
        'types.MessageEmpty',
        alias='_'
    )

    id: int
    peer_id: typing.Optional["base.Peer"] = None
