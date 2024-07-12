from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateUserStatus(BaseModel):
    """
    types.UpdateUserStatus
    ID: 0xe5bdf8de
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateUserStatus', 'UpdateUserStatus'] = pydantic.Field(
        'types.UpdateUserStatus',
        alias='_'
    )

    user_id: int
    status: "base.UserStatus"
