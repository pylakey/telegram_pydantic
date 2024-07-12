from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PremiumGiftOption(BaseModel):
    """
    types.PremiumGiftOption
    ID: 0x74c34319
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PremiumGiftOption', 'PremiumGiftOption'] = pydantic.Field(
        'types.PremiumGiftOption',
        alias='_'
    )

    months: int
    currency: str
    amount: int
    bot_url: str
    store_product: typing.Optional[str] = None
