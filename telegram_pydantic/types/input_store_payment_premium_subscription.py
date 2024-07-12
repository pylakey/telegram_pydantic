from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStorePaymentPremiumSubscription(BaseModel):
    """
    types.InputStorePaymentPremiumSubscription
    ID: 0xa6751e66
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStorePaymentPremiumSubscription', 'InputStorePaymentPremiumSubscription'] = pydantic.Field(
        'types.InputStorePaymentPremiumSubscription',
        alias='_'
    )

    restore: typing.Optional[bool] = None
    upgrade: typing.Optional[bool] = None
