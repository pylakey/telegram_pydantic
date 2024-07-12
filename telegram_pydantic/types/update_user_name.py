from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateUserName(BaseModel):
    """
    types.UpdateUserName
    ID: 0xa7848924
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateUserName', 'UpdateUserName'] = pydantic.Field(
        'types.UpdateUserName',
        alias='_'
    )

    user_id: int
    first_name: str
    last_name: str
    usernames: list["base.Username"]
