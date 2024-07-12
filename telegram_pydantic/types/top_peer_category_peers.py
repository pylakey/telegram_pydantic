from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeerCategoryPeers(BaseModel):
    """
    types.TopPeerCategoryPeers
    ID: 0xfb834291
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeerCategoryPeers', 'TopPeerCategoryPeers'] = pydantic.Field(
        'types.TopPeerCategoryPeers',
        alias='_'
    )

    category: "base.TopPeerCategory"
    count: int
    peers: list["base.TopPeer"]
