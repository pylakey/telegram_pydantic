from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CancelPasswordEmail(BaseModel):
    """
    functions.account.CancelPasswordEmail
    ID: 0xc1cbd5b6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.CancelPasswordEmail', 'CancelPasswordEmail'] = pydantic.Field(
        'functions.account.CancelPasswordEmail',
        alias='_'
    )

