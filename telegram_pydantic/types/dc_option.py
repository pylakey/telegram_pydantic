from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DcOption(BaseModel):
    """
    types.DcOption
    ID: 0x18b7a10d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DcOption', 'DcOption'] = pydantic.Field(
        'types.DcOption',
        alias='_'
    )

    id: int
    ip_address: str
    port: int
    ipv6: typing.Optional[bool] = None
    media_only: typing.Optional[bool] = None
    tcpo_only: typing.Optional[bool] = None
    cdn: typing.Optional[bool] = None
    static: typing.Optional[bool] = None
    this_port_only: typing.Optional[bool] = None
    secret: typing.Optional[Bytes] = None
