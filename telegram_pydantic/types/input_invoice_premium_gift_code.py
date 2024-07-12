from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputInvoicePremiumGiftCode(BaseModel):
    """
    types.InputInvoicePremiumGiftCode
    ID: 0x98986c0d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputInvoicePremiumGiftCode', 'InputInvoicePremiumGiftCode'] = pydantic.Field(
        'types.InputInvoicePremiumGiftCode',
        alias='_'
    )

    purpose: "base.InputStorePaymentPurpose"
    option: "base.PremiumGiftCodeOption"
