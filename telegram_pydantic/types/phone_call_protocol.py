from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallProtocol(BaseModel):
    """
    types.PhoneCallProtocol
    ID: 0xfc878fc8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallProtocol', 'PhoneCallProtocol'] = pydantic.Field(
        'types.PhoneCallProtocol',
        alias='_'
    )

    min_layer: int
    max_layer: int
    library_versions: list[str]
    udp_p2p: typing.Optional[bool] = None
    udp_reflector: typing.Optional[bool] = None
