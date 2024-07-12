from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueErrorFiles(BaseModel):
    """
    types.SecureValueErrorFiles
    ID: 0x666220e9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueErrorFiles', 'SecureValueErrorFiles'] = pydantic.Field(
        'types.SecureValueErrorFiles',
        alias='_'
    )

    type: "base.SecureValueType"
    file_hash: list[Bytes]
    text: str
