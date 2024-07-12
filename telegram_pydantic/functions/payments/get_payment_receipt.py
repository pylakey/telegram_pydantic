from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPaymentReceipt(BaseModel):
    """
    functions.payments.GetPaymentReceipt
    ID: 0x2478d1cc
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.GetPaymentReceipt', 'GetPaymentReceipt'] = pydantic.Field(
        'functions.payments.GetPaymentReceipt',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
