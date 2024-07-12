from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPeerChannel(BaseModel):
    """
    types.InputPeerChannel
    ID: 0x27bcbbfc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPeerChannel', 'InputPeerChannel'] = pydantic.Field(
        'types.InputPeerChannel',
        alias='_'
    )

    channel_id: int
    access_hash: int
