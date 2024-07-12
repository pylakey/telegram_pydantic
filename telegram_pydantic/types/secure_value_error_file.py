from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueErrorFile(BaseModel):
    """
    types.SecureValueErrorFile
    ID: 0x7a700873
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueErrorFile', 'SecureValueErrorFile'] = pydantic.Field(
        'types.SecureValueErrorFile',
        alias='_'
    )

    type: "base.SecureValueType"
    file_hash: Bytes
    text: str
