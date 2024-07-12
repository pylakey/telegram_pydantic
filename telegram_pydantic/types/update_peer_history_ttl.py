from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePeerHistoryTTL(BaseModel):
    """
    types.UpdatePeerHistoryTTL
    ID: 0xbb9bb9a5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePeerHistoryTTL', 'UpdatePeerHistoryTTL'] = pydantic.Field(
        'types.UpdatePeerHistoryTTL',
        alias='_'
    )

    peer: "base.Peer"
    ttl_period: typing.Optional[int] = None
