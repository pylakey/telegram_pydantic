from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ShippingOption(BaseModel):
    """
    types.ShippingOption
    ID: 0xb6213cdf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ShippingOption', 'ShippingOption'] = pydantic.Field(
        'types.ShippingOption',
        alias='_'
    )

    id: str
    title: str
    prices: list["base.LabeledPrice"]
