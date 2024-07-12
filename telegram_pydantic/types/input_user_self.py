from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputUserSelf(BaseModel):
    """
    types.InputUserSelf
    ID: 0xf7c1b13f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputUserSelf', 'InputUserSelf'] = pydantic.Field(
        'types.InputUserSelf',
        alias='_'
    )

