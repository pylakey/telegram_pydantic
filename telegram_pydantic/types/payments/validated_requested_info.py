from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ValidatedRequestedInfo(BaseModel):
    """
    types.payments.ValidatedRequestedInfo
    ID: 0xd1451883
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.ValidatedRequestedInfo', 'ValidatedRequestedInfo'] = pydantic.Field(
        'types.payments.ValidatedRequestedInfo',
        alias='_'
    )

    id: typing.Optional[str] = None
    shipping_options: typing.Optional[list["base.ShippingOption"]] = None
