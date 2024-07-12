from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmailVerificationGoogle(BaseModel):
    """
    types.EmailVerificationGoogle
    ID: 0xdb909ec2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmailVerificationGoogle', 'EmailVerificationGoogle'] = pydantic.Field(
        'types.EmailVerificationGoogle',
        alias='_'
    )

    token: str
