from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePeerSettings(BaseModel):
    """
    types.UpdatePeerSettings
    ID: 0x6a7e7366
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePeerSettings', 'UpdatePeerSettings'] = pydantic.Field(
        'types.UpdatePeerSettings',
        alias='_'
    )

    peer: "base.Peer"
    settings: "base.PeerSettings"
