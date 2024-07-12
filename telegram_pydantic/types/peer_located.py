from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerLocated(BaseModel):
    """
    types.PeerLocated
    ID: 0xca461b5d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerLocated', 'PeerLocated'] = pydantic.Field(
        'types.PeerLocated',
        alias='_'
    )

    peer: "base.Peer"
    expires: Datetime
    distance: int
