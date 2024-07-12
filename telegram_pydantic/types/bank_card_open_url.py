from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BankCardOpenUrl(BaseModel):
    """
    types.BankCardOpenUrl
    ID: 0xf568028a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BankCardOpenUrl', 'BankCardOpenUrl'] = pydantic.Field(
        'types.BankCardOpenUrl',
        alias='_'
    )

    url: str
    name: str
