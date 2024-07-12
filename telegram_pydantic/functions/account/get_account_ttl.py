from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAccountTTL(BaseModel):
    """
    functions.account.GetAccountTTL
    ID: 0x8fc711d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetAccountTTL', 'GetAccountTTL'] = pydantic.Field(
        'functions.account.GetAccountTTL',
        alias='_'
    )

