from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BindTempAuthKey(BaseModel):
    """
    functions.auth.BindTempAuthKey
    ID: 0xcdd42a05
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.BindTempAuthKey', 'BindTempAuthKey'] = pydantic.Field(
        'functions.auth.BindTempAuthKey',
        alias='_'
    )

    perm_auth_key_id: int
    nonce: int
    expires_at: Datetime
    encrypted_message: Bytes
