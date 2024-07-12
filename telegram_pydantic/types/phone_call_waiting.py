from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallWaiting(BaseModel):
    """
    types.PhoneCallWaiting
    ID: 0xc5226f17
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallWaiting', 'PhoneCallWaiting'] = pydantic.Field(
        'types.PhoneCallWaiting',
        alias='_'
    )

    id: int
    access_hash: int
    date: Datetime
    admin_id: int
    participant_id: int
    protocol: "base.PhoneCallProtocol"
    video: typing.Optional[bool] = None
    receive_date: Datetime
