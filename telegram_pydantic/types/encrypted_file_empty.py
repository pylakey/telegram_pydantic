from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedFileEmpty(BaseModel):
    """
    types.EncryptedFileEmpty
    ID: 0xc21f497e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedFileEmpty', 'EncryptedFileEmpty'] = pydantic.Field(
        'types.EncryptedFileEmpty',
        alias='_'
    )

