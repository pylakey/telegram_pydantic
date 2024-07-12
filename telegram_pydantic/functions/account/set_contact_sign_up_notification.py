from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetContactSignUpNotification(BaseModel):
    """
    functions.account.SetContactSignUpNotification
    ID: 0xcff43f61
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SetContactSignUpNotification', 'SetContactSignUpNotification'] = pydantic.Field(
        'functions.account.SetContactSignUpNotification',
        alias='_'
    )

    silent: bool
