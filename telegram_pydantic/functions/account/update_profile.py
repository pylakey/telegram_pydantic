from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateProfile(BaseModel):
    """
    functions.account.UpdateProfile
    ID: 0x78515775
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateProfile', 'UpdateProfile'] = pydantic.Field(
        'functions.account.UpdateProfile',
        alias='_'
    )

    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    about: typing.Optional[str] = None
