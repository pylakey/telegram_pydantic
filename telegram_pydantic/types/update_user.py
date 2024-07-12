from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateUser(BaseModel):
    """
    types.UpdateUser
    ID: 0x20529438
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateUser', 'UpdateUser'] = pydantic.Field(
        'types.UpdateUser',
        alias='_'
    )

    user_id: int
