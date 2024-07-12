from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Username(BaseModel):
    """
    types.Username
    ID: 0xb4073647
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Username', 'Username'] = pydantic.Field(
        'types.Username',
        alias='_'
    )

    username: str
    editable: typing.Optional[bool] = None
    active: typing.Optional[bool] = None
