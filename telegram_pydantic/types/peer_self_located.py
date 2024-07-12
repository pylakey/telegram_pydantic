from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerSelfLocated(BaseModel):
    """
    types.PeerSelfLocated
    ID: 0xf8ec284b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerSelfLocated', 'PeerSelfLocated'] = pydantic.Field(
        'types.PeerSelfLocated',
        alias='_'
    )

    expires: Datetime
