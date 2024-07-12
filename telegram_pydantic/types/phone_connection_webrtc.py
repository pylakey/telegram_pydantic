from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneConnectionWebrtc(BaseModel):
    """
    types.PhoneConnectionWebrtc
    ID: 0x635fe375
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneConnectionWebrtc', 'PhoneConnectionWebrtc'] = pydantic.Field(
        'types.PhoneConnectionWebrtc',
        alias='_'
    )

    id: int
    ip: str
    ipv6: str
    port: int
    username: str
    password: str
    turn: typing.Optional[bool] = None
    stun: typing.Optional[bool] = None
