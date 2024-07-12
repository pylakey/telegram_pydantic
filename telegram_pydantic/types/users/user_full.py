from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserFull(BaseModel):
    """
    types.users.UserFull
    ID: 0x3b6d152e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.users.UserFull', 'UserFull'] = pydantic.Field(
        'types.users.UserFull',
        alias='_'
    )

    full_user: "base.UserFull"
    chats: list["base.Chat"]
    users: list["base.User"]
