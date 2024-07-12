from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerBlocked(BaseModel):
    """
    types.PeerBlocked
    ID: 0xe8fd8014
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerBlocked', 'PeerBlocked'] = pydantic.Field(
        'types.PeerBlocked',
        alias='_'
    )

    peer_id: "base.Peer"
    date: Datetime
