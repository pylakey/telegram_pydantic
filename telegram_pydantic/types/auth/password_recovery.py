from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PasswordRecovery(BaseModel):
    """
    types.auth.PasswordRecovery
    ID: 0x137948a5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.PasswordRecovery', 'PasswordRecovery'] = pydantic.Field(
        'types.auth.PasswordRecovery',
        alias='_'
    )

    email_pattern: str
