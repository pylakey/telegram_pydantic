from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ImportBotAuthorization(BaseModel):
    """
    functions.auth.ImportBotAuthorization
    ID: 0x67a3ff2c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.ImportBotAuthorization', 'ImportBotAuthorization'] = pydantic.Field(
        'functions.auth.ImportBotAuthorization',
        alias='_'
    )

    flags: int
    api_id: int
    api_hash: str
    bot_auth_token: str
