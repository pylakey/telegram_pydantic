from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallAccepted(BaseModel):
    """
    types.PhoneCallAccepted
    ID: 0x3660c311
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallAccepted', 'PhoneCallAccepted'] = pydantic.Field(
        'types.PhoneCallAccepted',
        alias='_'
    )

    id: int
    access_hash: int
    date: Datetime
    admin_id: int
    participant_id: int
    g_b: Bytes
    protocol: "base.PhoneCallProtocol"
    video: typing.Optional[bool] = None
