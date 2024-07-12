from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AssignAppStoreTransaction(BaseModel):
    """
    functions.payments.AssignAppStoreTransaction
    ID: 0x80ed747d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.AssignAppStoreTransaction', 'AssignAppStoreTransaction'] = pydantic.Field(
        'functions.payments.AssignAppStoreTransaction',
        alias='_'
    )

    receipt: Bytes
    purpose: "base.InputStorePaymentPurpose"
