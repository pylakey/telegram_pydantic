from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerChannel(BaseModel):
    """
    types.PeerChannel
    ID: 0xa2a5371e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerChannel', 'PeerChannel'] = pydantic.Field(
        'types.PeerChannel',
        alias='_'
    )

    channel_id: int
