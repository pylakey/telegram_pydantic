from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecoverPassword(BaseModel):
    """
    functions.auth.RecoverPassword
    ID: 0x37096c70
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.RecoverPassword', 'RecoverPassword'] = pydantic.Field(
        'functions.auth.RecoverPassword',
        alias='_'
    )

    code: str
    new_settings: typing.Optional["base.account.PasswordInputSettings"] = None
