from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallRequested(BaseModel):
    """
    types.PhoneCallRequested
    ID: 0x14b0ed0c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallRequested', 'PhoneCallRequested'] = pydantic.Field(
        'types.PhoneCallRequested',
        alias='_'
    )

    id: int
    access_hash: int
    date: Datetime
    admin_id: int
    participant_id: int
    g_a_hash: Bytes
    protocol: "base.PhoneCallProtocol"
    video: typing.Optional[bool] = None
