from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmailVerified(BaseModel):
    """
    types.account.EmailVerified
    ID: 0x2b96cd1b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.EmailVerified', 'EmailVerified'] = pydantic.Field(
        'types.account.EmailVerified',
        alias='_'
    )

    email: str
