from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SignIn(BaseModel):
    """
    functions.auth.SignIn
    ID: 0x8d52a951
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.SignIn', 'SignIn'] = pydantic.Field(
        'functions.auth.SignIn',
        alias='_'
    )

    phone_number: str
    phone_code_hash: str
    phone_code: typing.Optional[str] = None
    email_verification: typing.Optional["base.EmailVerification"] = None
