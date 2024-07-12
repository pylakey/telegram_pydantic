from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputClientProxy(BaseModel):
    """
    types.InputClientProxy
    ID: 0x75588b3f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputClientProxy', 'InputClientProxy'] = pydantic.Field(
        'types.InputClientProxy',
        alias='_'
    )

    address: str
    port: int
