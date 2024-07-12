from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PasswordInputSettings(BaseModel):
    """
    types.account.PasswordInputSettings
    ID: 0xc23727c9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.PasswordInputSettings', 'PasswordInputSettings'] = pydantic.Field(
        'types.account.PasswordInputSettings',
        alias='_'
    )

    new_algo: typing.Optional["base.PasswordKdfAlgo"] = None
    new_password_hash: typing.Optional[Bytes] = None
    hint: typing.Optional[str] = None
    email: typing.Optional[str] = None
    new_secure_settings: typing.Optional["base.SecureSecretSettings"] = None
