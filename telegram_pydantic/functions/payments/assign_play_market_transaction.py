from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AssignPlayMarketTransaction(BaseModel):
    """
    functions.payments.AssignPlayMarketTransaction
    ID: 0xdffd50d3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.AssignPlayMarketTransaction', 'AssignPlayMarketTransaction'] = pydantic.Field(
        'functions.payments.AssignPlayMarketTransaction',
        alias='_'
    )

    receipt: "base.DataJSON"
    purpose: "base.InputStorePaymentPurpose"
