from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestedPeerChannel(BaseModel):
    """
    types.RequestedPeerChannel
    ID: 0x8ba403e4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RequestedPeerChannel', 'RequestedPeerChannel'] = pydantic.Field(
        'types.RequestedPeerChannel',
        alias='_'
    )

    channel_id: int
    title: typing.Optional[str] = None
    username: typing.Optional[str] = None
    photo: typing.Optional["base.Photo"] = None
