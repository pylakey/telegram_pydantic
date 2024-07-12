from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChangeAuthorizationSettings(BaseModel):
    """
    functions.account.ChangeAuthorizationSettings
    ID: 0x40f48462
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ChangeAuthorizationSettings', 'ChangeAuthorizationSettings'] = pydantic.Field(
        'functions.account.ChangeAuthorizationSettings',
        alias='_'
    )

    hash: int
    confirmed: typing.Optional[bool] = None
    encrypted_requests_disabled: typing.Optional[bool] = None
    call_requests_disabled: typing.Optional[bool] = None
