from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RefundStarsCharge(BaseModel):
    """
    functions.payments.RefundStarsCharge
    ID: 0x25ae8f4a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.RefundStarsCharge', 'RefundStarsCharge'] = pydantic.Field(
        'functions.payments.RefundStarsCharge',
        alias='_'
    )

    user_id: "base.InputUser"
    charge_id: str
