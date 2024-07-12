from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Error(BaseModel):
    """
    types.Error
    ID: 0xc4b9f9bb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Error', 'Error'] = pydantic.Field(
        'types.Error',
        alias='_'
    )

    code: int
    text: str
