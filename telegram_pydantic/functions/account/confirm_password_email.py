from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ConfirmPasswordEmail(BaseModel):
    """
    functions.account.ConfirmPasswordEmail
    ID: 0x8fdf1920
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ConfirmPasswordEmail', 'ConfirmPasswordEmail'] = pydantic.Field(
        'functions.account.ConfirmPasswordEmail',
        alias='_'
    )

    code: str
