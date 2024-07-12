from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserInfo(BaseModel):
    """
    types.help.UserInfo
    ID: 0x1eb3758
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.UserInfo', 'UserInfo'] = pydantic.Field(
        'types.help.UserInfo',
        alias='_'
    )

    message: str
    entities: list["base.MessageEntity"]
    author: str
    date: Datetime
