from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RegisterDevice(BaseModel):
    """
    functions.account.RegisterDevice
    ID: 0xec86017a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.RegisterDevice', 'RegisterDevice'] = pydantic.Field(
        'functions.account.RegisterDevice',
        alias='_'
    )

    token_type: int
    token: str
    app_sandbox: bool
    secret: Bytes
    other_uids: list[int]
    no_muted: typing.Optional[bool] = None
