from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeclinePasswordReset(BaseModel):
    """
    functions.account.DeclinePasswordReset
    ID: 0x4c9409f6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.DeclinePasswordReset', 'DeclinePasswordReset'] = pydantic.Field(
        'functions.account.DeclinePasswordReset',
        alias='_'
    )

