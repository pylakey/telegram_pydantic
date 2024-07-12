from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputEncryptedFileBigUploaded(BaseModel):
    """
    types.InputEncryptedFileBigUploaded
    ID: 0x2dc173c8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputEncryptedFileBigUploaded', 'InputEncryptedFileBigUploaded'] = pydantic.Field(
        'types.InputEncryptedFileBigUploaded',
        alias='_'
    )

    id: int
    parts: int
    key_fingerprint: int
