from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetUsers(BaseModel):
    """
    functions.users.GetUsers
    ID: 0xd91a548
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.users.GetUsers', 'GetUsers'] = pydantic.Field(
        'functions.users.GetUsers',
        alias='_'
    )

    id: list["base.InputUser"]
