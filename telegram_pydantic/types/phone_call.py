from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCall(BaseModel):
    """
    types.PhoneCall
    ID: 0x30535af5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCall', 'PhoneCall'] = pydantic.Field(
        'types.PhoneCall',
        alias='_'
    )

    id: int
    access_hash: int
    date: Datetime
    admin_id: int
    participant_id: int
    g_a_or_b: Bytes
    key_fingerprint: int
    protocol: "base.PhoneCallProtocol"
    connections: list["base.PhoneConnection"]
    start_date: Datetime
    p2p_allowed: typing.Optional[bool] = None
    video: typing.Optional[bool] = None
    custom_parameters: typing.Optional["base.DataJSON"] = None
