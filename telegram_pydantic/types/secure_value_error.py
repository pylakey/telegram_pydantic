from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueError(BaseModel):
    """
    types.SecureValueError
    ID: 0x869d758f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueError', 'SecureValueError'] = pydantic.Field(
        'types.SecureValueError',
        alias='_'
    )

    type: "base.SecureValueType"
    hash: Bytes
    text: str
