from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ApplyGiftCode(BaseModel):
    """
    functions.payments.ApplyGiftCode
    ID: 0xf6e26854
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.ApplyGiftCode', 'ApplyGiftCode'] = pydantic.Field(
        'functions.payments.ApplyGiftCode',
        alias='_'
    )

    slug: str
