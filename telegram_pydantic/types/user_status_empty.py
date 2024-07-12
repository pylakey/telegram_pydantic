from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserStatusEmpty(BaseModel):
    """
    types.UserStatusEmpty
    ID: 0x9d05049
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UserStatusEmpty', 'UserStatusEmpty'] = pydantic.Field(
        'types.UserStatusEmpty',
        alias='_'
    )

