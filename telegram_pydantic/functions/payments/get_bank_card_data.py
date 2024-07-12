from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBankCardData(BaseModel):
    """
    functions.payments.GetBankCardData
    ID: 0x2e79d779
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.GetBankCardData', 'GetBankCardData'] = pydantic.Field(
        'functions.payments.GetBankCardData',
        alias='_'
    )

    number: str
