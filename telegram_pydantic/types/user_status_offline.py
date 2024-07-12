from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserStatusOffline(BaseModel):
    """
    types.UserStatusOffline
    ID: 0x8c703f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UserStatusOffline', 'UserStatusOffline'] = pydantic.Field(
        'types.UserStatusOffline',
        alias='_'
    )

    was_online: Datetime
