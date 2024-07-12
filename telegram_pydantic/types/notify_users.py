from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NotifyUsers(BaseModel):
    """
    types.NotifyUsers
    ID: 0xb4c83b4c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NotifyUsers', 'NotifyUsers'] = pydantic.Field(
        'types.NotifyUsers',
        alias='_'
    )

