from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestedPeerChat(BaseModel):
    """
    types.RequestedPeerChat
    ID: 0x7307544f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RequestedPeerChat', 'RequestedPeerChat'] = pydantic.Field(
        'types.RequestedPeerChat',
        alias='_'
    )

    chat_id: int
    title: typing.Optional[str] = None
    photo: typing.Optional["base.Photo"] = None
