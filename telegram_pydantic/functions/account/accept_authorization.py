from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AcceptAuthorization(BaseModel):
    """
    functions.account.AcceptAuthorization
    ID: 0xf3ed4c73
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.AcceptAuthorization', 'AcceptAuthorization'] = pydantic.Field(
        'functions.account.AcceptAuthorization',
        alias='_'
    )

    bot_id: int
    scope: str
    public_key: str
    value_hashes: list["base.SecureValueHash"]
    credentials: "base.SecureCredentialsEncrypted"
