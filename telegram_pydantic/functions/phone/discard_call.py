from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DiscardCall(BaseModel):
    """
    functions.phone.DiscardCall
    ID: 0xb2cbc1c0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.DiscardCall', 'DiscardCall'] = pydantic.Field(
        'functions.phone.DiscardCall',
        alias='_'
    )

    peer: "base.InputPhoneCall"
    duration: int
    reason: "base.PhoneCallDiscardReason"
    connection_id: int
    video: typing.Optional[bool] = None
