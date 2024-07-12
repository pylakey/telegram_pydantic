from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestCall(BaseModel):
    """
    functions.phone.RequestCall
    ID: 0x42ff96ed
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.RequestCall', 'RequestCall'] = pydantic.Field(
        'functions.phone.RequestCall',
        alias='_'
    )

    user_id: "base.InputUser"
    random_id: int
    g_a_hash: Bytes
    protocol: "base.PhoneCallProtocol"
    video: typing.Optional[bool] = None
