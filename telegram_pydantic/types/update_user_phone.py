from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateUserPhone(BaseModel):
    """
    types.UpdateUserPhone
    ID: 0x5492a13
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateUserPhone', 'UpdateUserPhone'] = pydantic.Field(
        'types.UpdateUserPhone',
        alias='_'
    )

    user_id: int
    phone: str
