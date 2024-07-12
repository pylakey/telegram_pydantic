from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResendPasswordEmail(BaseModel):
    """
    functions.account.ResendPasswordEmail
    ID: 0x7a7f2a15
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ResendPasswordEmail', 'ResendPasswordEmail'] = pydantic.Field(
        'functions.account.ResendPasswordEmail',
        alias='_'
    )

