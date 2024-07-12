from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneConnection(BaseModel):
    """
    types.PhoneConnection
    ID: 0x9cc123c7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneConnection', 'PhoneConnection'] = pydantic.Field(
        'types.PhoneConnection',
        alias='_'
    )

    id: int
    ip: str
    ipv6: str
    port: int
    peer_tag: Bytes
    tcp: typing.Optional[bool] = None
