from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserEmpty(BaseModel):
    """
    types.UserEmpty
    ID: 0xd3bc4b7a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UserEmpty', 'UserEmpty'] = pydantic.Field(
        'types.UserEmpty',
        alias='_'
    )

    id: int
