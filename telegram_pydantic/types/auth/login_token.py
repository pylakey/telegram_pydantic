from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LoginToken(BaseModel):
    """
    types.auth.LoginToken
    ID: 0x629f1980
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.LoginToken', 'LoginToken'] = pydantic.Field(
        'types.auth.LoginToken',
        alias='_'
    )

    expires: Datetime
    token: Bytes
