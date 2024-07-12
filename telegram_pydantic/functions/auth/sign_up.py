from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SignUp(BaseModel):
    """
    functions.auth.SignUp
    ID: 0xaac7b717
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.SignUp', 'SignUp'] = pydantic.Field(
        'functions.auth.SignUp',
        alias='_'
    )

    phone_number: str
    phone_code_hash: str
    first_name: str
    last_name: str
    no_joined_notifications: typing.Optional[bool] = None
