from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputEncryptedFile(BaseModel):
    """
    types.InputEncryptedFile
    ID: 0x5a17b5e5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputEncryptedFile', 'InputEncryptedFile'] = pydantic.Field(
        'types.InputEncryptedFile',
        alias='_'
    )

    id: int
    access_hash: int
