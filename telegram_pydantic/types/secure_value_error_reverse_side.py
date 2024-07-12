from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueErrorReverseSide(BaseModel):
    """
    types.SecureValueErrorReverseSide
    ID: 0x868a2aa5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueErrorReverseSide', 'SecureValueErrorReverseSide'] = pydantic.Field(
        'types.SecureValueErrorReverseSide',
        alias='_'
    )

    type: "base.SecureValueType"
    file_hash: Bytes
    text: str
