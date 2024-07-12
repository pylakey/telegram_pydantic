from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmailVerificationApple(BaseModel):
    """
    types.EmailVerificationApple
    ID: 0x96d074fd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmailVerificationApple', 'EmailVerificationApple'] = pydantic.Field(
        'types.EmailVerificationApple',
        alias='_'
    )

    token: str
