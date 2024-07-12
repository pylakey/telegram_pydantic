from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserStatusOnline(BaseModel):
    """
    types.UserStatusOnline
    ID: 0xedb93949
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UserStatusOnline', 'UserStatusOnline'] = pydantic.Field(
        'types.UserStatusOnline',
        alias='_'
    )

    expires: Datetime
