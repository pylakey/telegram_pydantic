from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckGiftCode(BaseModel):
    """
    functions.payments.CheckGiftCode
    ID: 0x8e51b4c1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.CheckGiftCode', 'CheckGiftCode'] = pydantic.Field(
        'functions.payments.CheckGiftCode',
        alias='_'
    )

    slug: str
