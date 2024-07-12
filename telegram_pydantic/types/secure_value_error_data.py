from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueErrorData(BaseModel):
    """
    types.SecureValueErrorData
    ID: 0xe8a40bd9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueErrorData', 'SecureValueErrorData'] = pydantic.Field(
        'types.SecureValueErrorData',
        alias='_'
    )

    type: "base.SecureValueType"
    data_hash: Bytes
    field: str
    text: str
