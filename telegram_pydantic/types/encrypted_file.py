from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedFile(BaseModel):
    """
    types.EncryptedFile
    ID: 0xa8008cd8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedFile', 'EncryptedFile'] = pydantic.Field(
        'types.EncryptedFile',
        alias='_'
    )

    id: int
    access_hash: int
    size: int
    dc_id: int
    key_fingerprint: int
