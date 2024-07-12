from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputSecureFileUploaded(BaseModel):
    """
    types.InputSecureFileUploaded
    ID: 0x3334b0f0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputSecureFileUploaded', 'InputSecureFileUploaded'] = pydantic.Field(
        'types.InputSecureFileUploaded',
        alias='_'
    )

    id: int
    parts: int
    md5_checksum: str
    file_hash: Bytes
    secret: Bytes
