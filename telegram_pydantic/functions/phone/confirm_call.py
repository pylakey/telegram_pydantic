from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ConfirmCall(BaseModel):
    """
    functions.phone.ConfirmCall
    ID: 0x2efe1722
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.ConfirmCall', 'ConfirmCall'] = pydantic.Field(
        'functions.phone.ConfirmCall',
        alias='_'
    )

    peer: "base.InputPhoneCall"
    g_a: Bytes
    key_fingerprint: int
    protocol: "base.PhoneCallProtocol"
