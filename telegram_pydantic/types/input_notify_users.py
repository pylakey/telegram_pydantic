from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputNotifyUsers(BaseModel):
    """
    types.InputNotifyUsers
    ID: 0x193b4417
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputNotifyUsers', 'InputNotifyUsers'] = pydantic.Field(
        'types.InputNotifyUsers',
        alias='_'
    )

